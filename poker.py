"""
Create objects to handle modeling the game.
"""

from random import*
class Card():
    """ Rudimentary card class to track suit and value """
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
    def __repr__(self):
        """ Returns the value and suit of a card"""
        return str(self.value)+str(self.suit)
class CardSet():
    def __init__(self, cards = []):
        self.cards = cards
    def __repr__(self):
        """ Returns the value and suit of a card"""
    def add(self, card):
        """Adds an object to the hand"""
        self.cards.append(card)
    def remove(self, card):
        """Removes a spesific card from the hand"""
        for card in self.cards:
            if card.value == value and card.suit == suit:
                print("card removed")
                return self.cards.remove(card)
        print("error card not found")
class Deck(CardSet):
    def __init__(self):   
        Suits = ["C", "D", "S", "H"]
        Values = ["2","3","4","5","6","7","8","9","T","J","Q", "K", "A"]
        
        self.cards = []
        for s in Suits:
            for v in Values:
                self.add(v,s)

    def shuffle_deck(self):
        """Shuffles the deck"""
        # TODO: implement this
        pass

    def deal(self):
        """Returns the top card from the deck"""
        return self.cards.pop()
class Player():
    def __init__(self,funds, name):
        self.pocket = CardSet()
        self.funds = funds
        self.isturn = False
        self.folded = False
        self.wager = 0
        self.name = name

    def check(self):
        self.isturn = False

    def fold(self):
        self.folded = True

    def bet (self, bet, wager):

        self.wager = bet + wager
        self.isturn = False

    def call(self, wager):
        """player matches other player's bet"""
        self.wager = wager
        self.isturn = False
class Game():
    def __init__(self, money1, money2):
        round = ['preflop', 'flop', 'turn', 'river', 'showdown']
        self.communitycards = Cardset()
        self.deck = Deck()
        self.tablepot = 0
        self.player1_contribution = 0
        self.player2_contribution = 0
        self.smallblind_ammount = 50
        self.bigblind_ammount = 100
        self.player1 = Player(3000, "one")
        self.player2 = Player(3000, "two")
        self.round = 'preflop'

    def __repr__(self):
        print("Table Cards: " + str(self.communitycards))
        print("table Pot: " + str(self.tablepot.value))
        print("Player 1 Pocket: " + str(self.player1.hand.cards))
        print("Player1 Chips: " + str(self.player1.pot.value))
        print("Player 2 Pocket: " + str(self.player2.hand.cards))
        print("Player2 Chips: " + str(self.player2.pot.value))

    def betting():
        """Players bet against each other"""
        # TODO: implement this
        pass

    def preflop(self):
        # TODO: implement this
        # deal
        # bettting
        # advance to next round
        pass

    def flop(self):
        # TODO: implement this
        # deal
        # bettting
        # advance to next round
        pass

    def turn(self):
        # TODO: implement this
        # deal
        # bettting
        # advance to next round
        pass

    def river(self):
        # TODO: implement this
        # deal
        # bettting
        # advance to next round
        pass

    def showdown(self):
        """Finds Winner Gives Money"""
        # TODO: implement this
        pass

    def newround(self):
        self.table.cards = []
        self.player1.hand.cards =[]
        self.player2.hand.cards =[]
        self.player1.folded = False
        self.player2.folded = False

def comparehands(pocket1, pocket2, communitycards):
    """
    Takes two pockets plus community cards and returns WIN, LOSS, or DRAW with respect to the first hand
    """
    # TODO implement this
    pass
def handstrength(pocket, communitycards):
    """
    Takes a pocket and the community cards and returns the probability of winning the hand [0:1]
    """
    # TODO implement this
    pass
def deal(deck, cardset, quantity):
    """
    Removes the first 'quantiy' cards from the deck and adds them to the cardset
    """
    # TODO implement this
    pass

"""
Run game and accept inputs.
"""