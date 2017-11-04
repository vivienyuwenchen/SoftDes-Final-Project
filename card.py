from collections import defaultdict #frequwords
class Card():
    """ Grid world that contains Pauls (and other things) living in cells. """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
    	return("(%r %r)" % (  (self.suit),(self.value)))
        
class deck():
	def __init__(self):
		self.cards = []
	
	def add(self, num, suit):
		self.cards.append(Card(suit,num))

	def addcard(self, thiscard):
		self.cards.append(thiscard)

	def showcards(self):
		for card in self.cards:
			print(card.__repr__())
	def shuffle(self):
		random.shuffle(self.cards)

	def deal(self):
		return self.cards.pop()
class hand():
	def __init__(self):
		self.cards = []
	def add(self, card):
		self.cards.append(card)
	def showcards(self):
		for card in self.cards:
			print(card.__repr__())
	def remove_card(self, suit , value):
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
		self.cards.sort(key=lambda x: x.value, reverse=False)
		self.showcards()
	def has_twos(self):
		cardvalues = defaultdict(int)
		havevalues = []

		for card in self.cards:
			if card.value
			cardvalues[card.value] += 1


		
		




	


Suits = [" of clubs", " of Diamonds", " of Spades", " of Hearts"]
Values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
mydeck = deck()
for s in Suits:
	for v in Values:
		mydeck.add(v,s)
Ace = Card("of Spades", 13)
#print(Ace.__repr__())
#mydeck.showcards()
myhand = hand()
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
