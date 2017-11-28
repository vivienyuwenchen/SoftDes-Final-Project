#https://github.com/dennybritz/reinforcement-learning/tree/master/MC

import gym
from gym import spaces
from gym.utils import seeding
import control

class PokerEnv(gym.Env):
    """Simple poker environment
    The game starts with each player having two cards.

    The observation is a 2-tuple of: the players current hand strength and the amount of money on the table (0-100 dollars)

    The player can fold (0) or bet $1 (1)
    """
    def __init__(self):
        self.nA = 4             # number of actions

        self.action_space = spaces.Discrete(self.nA)
        self.observation_space = spaces.Tuple((
            spaces.Discrete(50),
            spaces.Discrete(100)))
        self._seed()

        self._reset()           # Start the first game

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _step(self, action):
        assert self.action_space.contains(action)
        if game.Player1.isturn:
            player = game.Player1
        else:
            player = game.Player2

        # Implement round progression? Reward given in showdown

        if action == 0:                                                         # check
            player.check()
        elif action == 1:                                                       # fold
            player.fold()
        elif action == 2:
            player.bet()                                                        # bet
        else:
            player.call()                                                       # call

        # If won, reward = + table_pot
        # If lost, reward = - wager
        self.reward = 0
        return self._get_obs(), self.reward, {}

    def _get_obs(self):
        hs = handstrength(game.Player1.pocket, game.community_cards)
        table_pot = game.table_plot
        wager = game.Player1.wager
        funds = game.Player1.funds

        wager2 = game.Player2.wager
        funds2 = game.Player2.funds


        return (hs, table_pot, wager, funds, wager2, funds2)

    def _reset(self):
        newround()

        return self._get_obs()
