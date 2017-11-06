def chen_hs(card1,card2):
	'''
		Returns the Chen formula hand strength for two cards.
		card = (suit, rank)
		rank : 2,3,4,5,6,7,8,9,10,J,Q,K,A
		suit : s,h,c,d
	'''
	score = 0

	#high card
	if card1[0] > card2[0]:
		high_card = str(card1[0])
	else : high_card = str(card2[0])
	
	if high_card == 'A' : score = 10
	elif high_card == 'K' : score = 8
	elif high_card == 'Q' : score = 7
	elif high_card == 'J' : score = 6
	else : score = int(high_card)/2

	#pairs
	is_pair = False
	if card1[0] == card2[0] : 
		score = score * 2
		is_pair = True

	#suited
	if card1[1] == card2[1] : score += 2

	return -(-score//1) 

card1 = ('A','c')
card2 = ('10','h')
print(chen_hs(card1,card2))

