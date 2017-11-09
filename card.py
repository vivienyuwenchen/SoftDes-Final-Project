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
		shuffle(self.cards)
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
	#def shuffle_deck(self):
		"""Shuffles the deck"""
	#	random.shuffle(self.cards)

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

	
	def __repr__(self):
		return self.value
class Player():
	def __init__(self,money):
		self.hand = Hand()
		self.pot = Pot(money)
		self.isturn = False
		self.folded = False
		self.bigblind = False
		self.smallblind = False
		self.contribution = 0
	def player_turn(self):
		""" is used to make it the player's turn"""
		self.isturn = True

	def player_showContribution(self):
		return(self.contribution)

	def player_check(self):
		self.isturn = False

	def player_fold(self):
		self.folded = True
		pass
	def player_contribute(self,money):
		"""
		store how much money the player added
		Pot add that money to the players pot contibution
		>>> player1 = Player(1000)
		>>> 
		>>> player1.player_contribute(100)

		>>> print (player1.contribution)
		100
		"""
		self.contribution += money
		

	def player_bet (self, raise_money,reciverpot):
		"""Takes the bet ammount and puts it in the pot
		>>> yourpot = Pot(10000)
		>>> player1 = Player(100000)
		>>> player1.player_bet(5000, yourpot)
		>>> print(yourpot.__repr__())
		15000"""
		
		self.pot.value -= raise_money
		reciverpot.value += raise_money
		self.isturn = False
		

	def player_call(self,call):
		"""player matches other player's bet"""
		other.money_to_pot(call, self.pot)
		self.isturn = False

		pass
class Game():
	def __repr__(self):
		print((self.table.cards))
		print(self.player1.hand.cards)
		pot = str(self.player1.pot.value)
		print(pot)
		print(self.player2.hand.cards)
		print(str(self.player2.pot.value))
	def __init__(self, money1, money2):
		self.table = Hand()
		self.deck = Deck()
		self.deck.createDeck()
		
		self.tablepot = Pot(0)
		self.player1_contribution = 0
		self.player2_contribution = 0
		self.smallblind_ammount = 50
		self.bigblind_ammount = 100
		self.player1 = Player(money1)
		self.player2 = Player(money2)

	def add_deck(self):
		"""Adds another deck if the first one runs low"""
		pass
	def pocket(self):
		"""deals each player 2 cards"""
		self.player1.hand.add(self.deck.deal())
		self.player2.hand.add(self.deck.deal())
		self.player1.hand.add(self.deck.deal())
		self.player2.hand.add(self.deck.deal())

		self.blinds(self.player1,self.player2)
		self.__repr__()
		self.player_move(self.player1,self.player2)




		pass
	def flop(self):
		self.table.add(self.deck.deal())
		self.table.add(self.deck.deal())
		self.table.add(self.deck.deal())
		self.player_move(self.player1,self.player2)

		"""puts three cards on the table"""
		pass
	def turn(self):
		"""puts one card on the table"""
		self.table.add(self.deck.deal())
		
		self.player_move(self.player1,self.player2)
		pass
	def river(self):
		"""puts one card on the table"""
		self.table.add(self.deck.deal())
		
		self.player_move(self.player1,self.player2)
		pass
	def showdown(self):
		"""Finds Winner Gives Money"""
		print("yay you made to the showdown")

	def counts_player_contrib(self,player, money, the_pot):
		""" when ever a player adds money to the table
		Pot add that money to the players pot contibution
		#>>> player1 = Player(1000)

		#>>> pot = Pot(100)

		#>>> Game.counts_player_contrib(player1, 100, pot)
		#100
		
		"""

		player.player_bet(money,the_pot)
		player.player_contribute(money)
		(player.player_showContribution())

	def blinds(self,player1, player2):
		"""chooses blinds for players"""
		if  player2.bigblind == False:
			player1.smallblind = True
			player2.bigblind = False
			player1.player_bet(self.smallblind_ammount,self.tablepot)
			player2.player_bet(self.bigblind_ammount,self.tablepot)

		if  player2.bigblind == True:
			player1.smallblind = True
			player2.bigblind = False
			player2.player_bet(self.smallblind_ammount,self.tablepot)
			player1.player_bet(self.bigblind_ammount,self.tablepot)

		
		
		pass
	def betting():
		"""players bet against each other"""
	def dealCards(self,deck, player1):
		"""
		pops cards of a deck and gives is to a player

		"""
		player1.addcard(deck.deal())

	def player_move(self,player, other):
		""" gets the move from the player"""
		move = input("Check, Raise, or Fold?>>>")
		if move == "Fold":
			player.player_fold()   #player folds
		elif move == "Check":
			#player maches the cotrobution of the other player
			
			if player.contribution < other.contribution: 
				money = other.contribution - player.contribution
				self.__repr__()
				player.player_bet(money, self.tablepot)

			
		elif move == "Raise": #player bets and abount
			money = 100
			player.player_bet(money, self.tablepot)
			self.__repr__()
			self.player_move(other,player)
		else:
			print("input error try again")
			self.player_move(self.player1,self.player2)



			#do nothing

#if __name__ == "__main__":
   # import doctest
#    doctest.testmod()
   # doctest.run_docstring_examples(Game.counts_player_contrib, globals(),verbose=True)
poker = Game(10000, 10000)
poker.pocket()

poker.flop()
poker.__repr__()
poker.turn()
poker.__repr__()
poker.river()
poker.__repr__()
poker.showdown()



#print(Ace.__repr__())
#mydeck.showcards()
#myhand = Hand()
#for i in range(5):
	#myhand.add(mydeck.deal())
#myhand.add(Card(" of Spades", 13))
#myhand.add(Card(" of Diamonds", 13))
#myhand.add(Card("of Spades", 12))
#myhand.add(Card(" of Hearts", 12))
#myhand.add(Card(" of clubs", 13))
#myhand.showcards()
#myhand.order()
#myhand.has_twos()
#mypot = Pot(10000)
#yourpot = Pot(10000)
#yourpot.money_to_pot(10000, mypot)
#print(mypot.__repr__())
#print(yourpot.__repr__())
#yourpot = Pot(10000)
#player1 = Player(100000)
#player1.player_bet(5000, yourpot)
##print(yourpot.__repr__())
#player2 = Player(100000)
#poker = Game(player1,player2,11,22)
#poker.deck.showcards()