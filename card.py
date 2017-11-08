from collections import defaultdict #frequwords
from random import*
class Card():
    """ Rudimentary card class to track suit and value """
    def __init__(self, suit, value):

        self.suit = suit
        self.value = value
    def __repr__(self):
    	""" Returns the value and suit of a card"""
    	return("(%r %r)" % (  (self.suit),(self.value)))
        
class Deck():
	def __init__(self):
		self.cards = []
	def createDeck(self):
		Suits = ["of clubs", "of Diamonds", "of Spades", "of Hearts"]
		Values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
		
		for s in Suits:
			for v in Values:
				self.add(s,v)
	def add(self, num, suit):
		"""Adds a card of value num and suit suit to the
		deck"""
		self.cards.append(Card(suit,num))

	def addcard(self, thiscard):
		"""Adds an object to the deck"""
		self.cards.append(thiscard)

	def showcards(self):
		"""Shows all of the cards in the deck"""
		for card in self.cards:
			print(card.__repr__())
	def shuffle(self):
		"""Shuffles the deck"""
		random.shuffle(self.cards)

	def deal(self):
		"""Returns the top card from the deck"""
		return self.cards.pop()
class Hand():
	def __init__(self):
		self.cards = []
	def add(self, card):
		"""Adds an object to the hand"""
		self.cards.append(card)
	def showcards(self):
		"""shows cards in the hand"""
		for card in self.cards:
			print(card.__repr__())
	def remove_card(self, suit , value):
		"""Removes a spesific card from the hand"""
		for card in self.cards:
			print (card.value)
			print (value)
			print (card.suit)
			print (suit)
			if card.value == value and card.suit == suit:
				print("card removed")
				return self.cards.remove(card)
		print("error card not found")
	def order(self):
		"""Orders the cards in the hand"""
		self.cards.sort(key=lambda x: x.value, reverse=False)
		self.showcards()
	def has_twos(self):
		"""Counts the number of each card in the hand
		puts results in a dict. """
		cardvalues = defaultdict(int)
		havevalues = []

		for card in self.cards:
			cardvalues[card.value] += 1
class Pot():
	def __init__(self, money):
		self.value = money

	def money_to_pot(self,money,other):
		"""moves money from the self pot into anouther
		pot"""
		self.value += money
		other.value -= money
	def __repr__(self):
		return self.value
class Player():
	def __init__(self,money):
		self.hand = Hand()
		self.pot = Pot(money)
		self.isturn = False
		self.folded = False
	def player_turn(self):
		""" is used to make it the player's turn"""
		self.isturn = True

	def player_check(self):
		self.isturn = False

	def player_fold(self):
		self.folded = True
		pass

	def player_bet (self, raise_money,other):
		"""Takes the bet ammount and puts it in the pot
		>>>yourpot = Pot(10000)
		>>>player1 = Player(100000)
		>>>player1.player_bet(5000, yourpot)
		>>>print(yourpot.__repr__())
		15000"""
		other.money_to_pot(raise_money, self.pot)
		self.isturn = False
		pass

	def player_call(self,call):
		"""player matches other player's bet"""
		other.money_to_pot(call, self.pot)
		self.isturn = False

		pass
class Game():
	def __init__(self, player1, money1, player2, money2):
		self.table = []
		self.deck = Deck()
		self.deck.createDeck()
	






		
		




	


Suits = [" of clubs", " of Diamonds", " of Spades", " of Hearts"]
Values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
mydeck = Deck()
for s in Suits:
	for v in Values:
		mydeck.add(s,v)
Ace = Card("of Spades", 13)
#print(Ace.__repr__())
#mydeck.showcards()
myhand = Hand()
#for i in range(5):
	#myhand.add(mydeck.deal())
myhand.add(Card(" of Spades", 13))
myhand.add(Card(" of Diamonds", 13))
myhand.add(Card("of Spades", 12))
myhand.add(Card(" of Hearts", 12))
myhand.add(Card(" of clubs", 13))
myhand.showcards()
myhand.order()
myhand.has_twos()
mypot = Pot(10000)
yourpot = Pot(10000)
yourpot.money_to_pot(10000, mypot)
print(mypot.__repr__())
print(yourpot.__repr__())
yourpot = Pot(10000)
player1 = Player(100000)
player1.player_bet(5000, yourpot)
print(yourpot.__repr__())
player2 = Player(100000)
poker = Game(player1,player2,11,22)
poker.deck.showcards()