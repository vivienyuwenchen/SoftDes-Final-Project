from pickle import dump, load
from collections import defaultdict

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

# cache = ['defaultdict(float)', 'defaultdict(float)', 'defaultdict(lambda: np.zeros(env.action_space.n))']
#
# dump_cache(cache, 'sa_cache.txt')
#
# new_cache = load_cache('sa_cache.txt')
# returns_sum = exec(new_cache[0])
# returns_count = exec(new_cache[1])
# Q = exec(new_cache[2])
#
# print("returns_sum:", returns_sum, ", returns_count:", returns_count, ", Q:", Q)
# print(type(returns_sum), type(returns_count), type(Q))

# https://github.com/dennybritz/reinforcement-learning/tree/master/MC

# https://github.com/dennybritz/reinforcement-learning/tree/master/MC

import gym
import matplotlib
import numpy as np
import sys
from pprint import pprint

from collections import defaultdict
from poker_env import PokerEnv

env = PokerEnv()

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

def mc_control_epsilon_greedy(env, num_episodes, discount_factor=1.0, epsilon=0.1):
    """
    Monte Carlo Control using Epsilon-Greedy policies. Finds an optimal epsilon-greedy policy.

    Args:
        env: OpenAI gym environment
        num_episodes: number of episodes to sample
        discount_factor: Lambda discount factor ???
        epsilon: Chance the sample a random action (float between 0 and 1)

    Returns:
        A tuple (Q, policy) where...
            Q is a dictionary mapping state -> action values
            Policy is a function that takes an observation as an argument and returns action probabilities
    """

    # Instatiate tracker of sum and count of returns for each state to calculate an average
    # returns_sum = defaultdict(float)
    # returns_count = defaultdict(float)


    # The action-value function -- a nested dictionary that maps state -> (action -> action-value).
    # Q = defaultdict(lambda: np.zeros(env.action_space.n))

    # The policy
    policy = make_epsilon_greedy_policy(Q, epsilon, env.action_space.n)

    for i_episode in range(1, num_episodes + 1):
        # Print out which episode we're on, useful for debugging.
        if i_episode % 1000 == 0:
            print("\rEpisode {}/{}.".format(i_episode, num_episodes), end="")
            sys.stdout.flush()

        # Generate an episode.
        # An episode is an array of (state, action, reward) tuples
        episode = []
        state = env.reset()
        for t in range(100):
            probs = policy(state)
            action = np.random.choice(np.arange(len(probs)), p=probs)
            #print("Action is: ", action)                                       # 0 or 1
            next_state, reward, _ = env.step(action)
            episode.append((state, action, reward))
            # if done:
            #     break
            state = next_state

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

    cache = [dict(returns_sum), dict(returns_count), dict(Q)]
    dump_cache(cache, 'sa_cache.txt')

    return Q, policy

Q, policy = mc_control_epsilon_greedy(env, num_episodes=5000, epsilon=0.1)

pprint( dict(Q) )
