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
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Tuple((
            spaces.Discrete(50),
            spaces.Discrete(100)))
        self._seed()

        # Start the first game
        self._reset()
        self.nA = 3             # number of actions

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _step(self, action):
        assert self.action_space.contains(action)
        if action:                                                                      # bet
            #self.player.append(draw_card(self.np_random))                              # use this line for placing additional cards on table
            self.table_money += 100
            if score(self.player) > score(self.dealer):
                self.reward = self.table_money
        else:                                                                           # fold
            self.reward = -self.table_money
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
        self.dealer = draw_hand(self.np_random)
        self.player = draw_hand(self.np_random)
        self.table_money = 100 # pretend blind is $1
        self.reward = 0

        return self._get_obs()
