from card import *

poker = Game(10000, 10000)
while True:
	poker.newround()

	if len(poker.deck.cards) < 20:
		poker.add_deck()

	poker.pocket()
	if poker.player1.folded == False and poker.player1.folded == False:
		poker.flop()
		poker.__repr__()
	if poker.player1.folded == False and poker.player1.folded == False:
		poker.turn()
		poker.__repr__()
	if poker.player1.folded == False and poker.player1.folded == False:
		poker.river()
		poker.__repr__()
	if poker.player1.folded == False and poker.player1.folded == False:
		poker.showdown()
	elif poker.player1.folded == True:
		poker.wins_Hand(poker.player2)
	else:
		poker.wins_Hand(poker.player1)
