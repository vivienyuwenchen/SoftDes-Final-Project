#https://github.com/dennybritz/reinforcement-learning/tree/master/MC

import gym
from gym import spaces
from gym.utils import seeding

# 2-10 = Number cards, Jack = 11, Queen = 12, King = 13, Ace = 14
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def draw_card(np_random):
    return np_random.choice(deck)

def draw_hand(np_random):
    return [draw_card(np_random), draw_card(np_random)]

def sum_hand(hand):  # Return current hand total
    if usable_ace(hand):
            return sum(hand) + 10
    return sum(hand)

def score(hand):
    card1 = hand[0]
    card2 = hand[1]
    score = 0

    if card1 > card2:
        high_card = card1
    else : high_card = card2

    score = high_card

	#pairs
    is_pair = False
    if card1 == card2:
        score = score * 2
        is_pair = True

	#suited
    if card1 == card2 : score += 2

	#gap
    gap = abs(card1 - card2)
    if gap == 1 : score += -1
    elif gap == 2 : score += -2
    elif gap == 3 : score += -4
    elif gap >= 4 : score += -5

	#correction
    if gap <= 1:
        if card1 < 13 and card2 < 13:
            score += 1

	#round up and return
    return -(-score//1)


class PokerEnv(gym.Env):
    """Simple poker environment
    The game starts with each player having two cards.

    The observation is a 2-tuple of: the players current hand strength and the amount of money on the table (0-100 dollars)

    The player can fold (0) or bet $1 (1)
    """
    def __init__(self):
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Tuple((
            spaces.Discrete(50),
            spaces.Discrete(100)))
        self._seed()

        # Start the first game
        self._reset()
        self.nA = 2             # number of actions

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _step(self, action):
        assert self.action_space.contains(action)
        if action:                                                                      # bet
            #self.player.append(draw_card(self.np_random))                              # use this line for placing additional cards on table
            self.table_money += 5
            if score(self.player) > score(self.dealer):
                self.reward = self.table_money
        else:                                                                           # fold
            self.reward = -self.table_money
        return self._get_obs(), self.reward, {}

    def _get_obs(self):
        return score(self.player)

    def _reset(self):
        self.dealer = draw_hand(self.np_random)
        self.player = draw_hand(self.np_random)
        self.table_money = 1 # pretend blind is $1
        self.reward = 0

        return self._get_obs()
