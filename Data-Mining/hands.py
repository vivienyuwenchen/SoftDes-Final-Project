
# Consider namedtuple for cases where you are using the class only to aggregate
# # data, not to add behavior (methods).
# For example:
#   from collections import namedtuple
#   Game = nametuple('Game', ['game_type', 'table', 'date', 'players', 'hands'])


class Game:
    """
    Contains the information for one complete game of poker
    """

    def __init__(self, game_type, table, date, players, hands):
        self.game_type = game_type
        self.table = table
        self.date = date
        self.players = players
        self.hands = hands


class Hand:
    """
    Contains the information for a full hand of poker

    Class documentation can also document the attributes. This isn't necessary
    for self-documenting names such as rounds. the type that isn't evident
    in this file is Hand.pot.
    """

    def __init__(self, rounds, dealer, stage_num, pot, table_cards, summary):
        self.rounds = rounds
        self.dealer = dealer
        self.stage_num = stage_num
        # In general, *remove* eliminated code such as the following.
        # Second best is to add a comment explaining *why* it is commented out,
        # and under what conditions it can be restored.
        #self.blinds = blinds
        # dealer always has small blind
        self.pot = pot
        self.table_cards = table_cards
        self.summary = summary


class Player:
    """
    Contains the information for one of the players
    """

    def __init__(self, player_id, starting_chips, is_dealer, pocket_cards, blind_amo):
        self.player_id = player_id
        self.starting_chips = starting_chips
        self.is_dealer = is_dealer
        self.pocket_cards = pocket_cards
        self.blind_amo = blind_amo


class Round:
    """
    Contains the information for one round of a hand of poker
    """

    def __init__(self, round_type, players, actions):
        #pocket, flop, turn, river, showdown
        self.round_type = round_type
        self.players = players
        self.actions = actions


class Action:
    """
    Tells action type and amount bet
    """

    def __init__(self, action_type, amount):
        # call, raise, check, fold
        self.action_type = action_type
        self.amount = amount

    def add_to_pot(self):
        act = self.action_type
        if act not in ['check', 'call', 'raise', 'fold']:
            raise Exception('not a valid action: ' + act)
