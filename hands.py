class Game:
    """
    Contains the information for one complete game of poker
    """
    def __init__(self, game_type, table, players, hands):
        self.game_type = game_type
        self.table = table
        self.players = players
        self.hands = hands

class Hand:
    """
    Contains the information for a full hand of poker
    """
    def __init__(self, dealer, stage_num, pot, table_cards, summary):
        self.dealer = dealer
        self.stage_num = stage_num
        #self.blinds = blinds
        #dealer always has small blind
        self.pot = pot
        self.table_cards = table_cards
        self.summary = summary

class Player:
    """
    Contains the information for one of the players
    """
    def __init__(self, player_id, starting_chips, is_dealer, pocket_cards):
        self.player_id = player_id
        self.starting_chips = starting_chips
        self.is_dealer = is_dealer
        self.pocket_cards = pocket_cards

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
        #call, raise, check, fold
        self.action_type = action_type
        self.amount = amount

    def add_to_pot(self):
        act = self.action_type
        if act == 'check':
            no change
        elif act == 'call':
            add to pot
        elif act == 'raise':
            add to pot
            also add the call amount?
        elif act == 'fold':
            no change
        else:
            print('not a valid action: '+act)
        pass
