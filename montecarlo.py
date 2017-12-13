"""
Trains bot using reinforcement learning. Called during training as well as during regular games.
"""

import matplotlib
import numpy as np
import sys
from pprint import pprint
from pickle import dump, load
from collections import defaultdict
from poker import *

def load_cache(file_name):
    """
    Args:
        file_name: name of file to read from
    Returns:
        text from file
    """
    file_ = open(file_name, 'rb+')
    return load(file_)

def dump_cache(text, file_name):
    """
    Args:
        text: text, i.e. state-action dictionary, that you want to dump into cache
        file_name: name of file to write to
    Returns:
        None
    """
    file_ = open(file_name, 'wb')
    dump(text, file_)

def make_epsilon_greedy_policy(Q, epsilon, nA):
    """
    Args:
        Q: dictionary that maps from state -> action-values.
        epsilon: probability to select a random action (float between 0 and 1)
        nA: number of actions in the environment

    Returns:
        A function that takes the observation as an argument and returns the probabilities for each action in the form of a numpy array of length nA.

    """
    def policy_fn(observation):
        A = np.ones(nA, dtype=float) * epsilon / nA                             # initialize probabilities (equal, normalized)
        best_action = np.argmax(Q[observation])                                 # find best action given observation
        A[best_action] += (1.0 - epsilon)                                       # bias towards performing best action
        return A                                                                # return probabilities of all actions
    return policy_fn                                                    # return function that given state, returns action probs

def mc_control_epsilon_greedy(episode, game, player, discount_factor=1.0, epsilon=0.1):
    """
    Monte Carlo Control using Epsilon-Greedy policies. Finds an optimal epsilon-greedy policy.

    Args:
        episode: list of (state, action, rewards) for entire game
        game: all information about current game in game class
        player: bot player class
        discount_factor: Lambda discount factor ???
        epsilon: Chance the sample a random action (float between 0 and 1)

    Returns:
        Action recommendation from bot
    """
    pocket = player.pocket.cards
    print(pocket)
    #there was a problem here with returning none, as an eventual heads up
    #print(pocket.cards)

    # Load dictionaries from file and convert to default dictionaries
    cache = load_cache('sa_cache.txt')
    returns_sum = defaultdict(float, cache[0])
    returns_count = defaultdict(float, cache[1])
    Q = defaultdict(lambda: np.zeros(3), cache[2])

    # The policy
    policy = make_epsilon_greedy_policy(Q, epsilon, 3) # (Q, E, nA)

    # Populate episode for current game
    # An episode is an array of (state, action, reward) tuples
    move = ''
    state = hand_strength(pocket[0], pocket[1])

    probs = policy(state)
    action = np.random.choice(np.arange(len(probs)), p=probs)
    if player.funds - 100 < 0:
        # hard code to fold if out of money to prevent raising cycle
        action = 0

    if game.round != 'showdown':
        if action == 0:
            move = "fold"
        elif action == 1:
            move = "raise"
        elif action == 2:
            move = "match"

    reward = 0
    episode.append([state, action, reward])

    if game.round == 'showdown':                                                         # only reward during showdown
        if game.winner == "TIE":                                                # reward pot amount if win or tie
            reward = game.table_pot/2
        elif game.winner == player.name:
            reward = game.table_pot
        else:                                                                   # negative reward (money lost) for loss
            reward = -player.wager

    for inc in episode:                                                         # backpropogate reward for all moves made in game (TODO: make incremental + probabalistic)
        inc[2] = reward

    # Find all (state, action) pairs we've visited in this episode
    # We convert each state to a tuple so that we can use it as a dict key

    sa_in_episode = set([(x[0], x[1]) for x in episode])
    for state, action in sa_in_episode:
        sa_pair = (state, action)
        # Find the first occurance of the (state, action) pair in the episode
        first_occurence_idx = next(i for i,x in enumerate(episode)
                                   if x[0] == state and x[1] == action)
        # Sum up all rewards since the first occurance
        G = sum([x[2]*(discount_factor**i) for i,x in enumerate(episode[first_occurence_idx:])])
        # Calculate average return for this state over all sampled episodes
        returns_sum[sa_pair] += G
        returns_count[sa_pair] += 1.0
        Q[state][action] = returns_sum[sa_pair] / returns_count[sa_pair]
        #print("For state ", state, "and action ", action, "reward is: ", Q[state][action])

    # Convert default dictionaries to dictionaries and dump into file
    cache = [dict(returns_sum), dict(returns_count), dict(Q)]
    dump_cache(cache, 'sa_cache.txt')

    return move
