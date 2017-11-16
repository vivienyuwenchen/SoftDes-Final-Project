def chen_hs(card1,card2):
	'''
		Returns the Chen formula hand strength for two cards.
		card = (str : suit, str : rank)
		rank : 2,3,4,5,6,7,8,9,10,J,Q,K,A
		suit : s,h,c,d
	'''
	score = 0
	value = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}

	#high card
	if value[card1[0]] > value[card2[0]]:
		high_card = card1[0]
	else : high_card = card2[0]
	
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

	#gap
	gap = abs(value[card1[0]]-value[card2[0]])
	if gap == 1 : score += -1
	elif gap == 2 : score += -2
	elif gap == 3 : score += -4
	elif gap >= 4 : score += -5

	#correction
	if gap <= 1:
		if value[card1[0]] < value['Q'] and value[card2[0]] < value['Q']:
			score += 1

	#round up and return
	return -(-score//1) 

card1 = ('A','c')
card2 = ('10','h')
print(chen_hs(card1,card2))

