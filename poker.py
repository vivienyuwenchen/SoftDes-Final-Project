"""
Create objects to handle modeling the game.
"""
# import bot
# import hand strength calculator
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
        pass
    def __repr__(self):
        """ Returns the value and suit of a card"""
        pass
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
    def __init__(self,funds, name, is_bot = False):
        self.pocket = CardSet()
        self.funds = funds
        self.isturn = False
        self.folded = False
        self.wager = 0
        self.name = name
        self.is_bot = is_bot
    def check(self):
        self.isturn = False
        pass
    def fold(self):
        self.folded = True
        pass
    def bet (self, bet, wager):
        self.wager = bet + wager
        self.isturn = False
        pass
    def call(self, wager):
        """player matches other player's bet"""
        self.wager = wager
        self.isturn = False
class Game():
    def __init__(self):
        self.round_name = ['preflop', 'flop', 'turn', 'river', 'showdown']
        self.communitycards = Cardset()
        self.deck = Deck()
        self.tablepot = 0
        self.smallblind_ammount = 50
        self.bigblind_ammount = 100
        self.player1 = Player(3000, "one")
        self.player2 = Player(3000, "two")
        self.round = 0
    def __repr__(self):
        print("Table Cards: " + str(self.communitycards))
        print("table Pot: " + str(self.tablepot.value))
        print("Player 1 Pocket: " + str(self.player1.hand.cards))
        print("Player1 Chips: " + str(self.player1.pot.value))
        print("Player 2 Pocket: " + str(self.player2.hand.cards))
        print("Player2 Chips: " + str(self.player2.pot.value))

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
Run game and accept inputs. Could split document here.
"""
# import viewer 

game = Game()
# initialize viewer
# viwer takes as input game and displays table

def get_input(player):
    """
    Get user or bot input.
    """
    # TODO: impliment this
    # if player.is_bot :
    # else:
    pass
def betting():
    """Players bet against each other"""
    # TODO: implement this
    # playerA bets
    # playerB bets
    # if playerA.wager = playerB.wager : return not folded
    # elif playerA.folded or playerB.folded : return folded
    # else repeat
    pass
def newround():
    self.table.cards = []
    self.player1.hand.cards =[]
    self.player2.hand.cards =[]
    self.player1.folded = False
    self.player2.folded = False
def preflop():
    # TODO: implement this
    # deal
    # bettting
    # advance to next round
    pass
def flop():
    # TODO: implement this
    # deal
    # bettting
    # advance to next round
    pass
def turn():
    # TODO: implement this
    # deal
    # bettting
    # advance to next round
    pass
def river():
    # TODO: implement this
    # deal
    # bettting
    # advance to next round
    pass
def showdown():
    """Finds Winner Gives Money"""
    # TODO: implement this
    # return winner
    pass


