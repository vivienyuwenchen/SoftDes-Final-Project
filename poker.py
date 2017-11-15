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
class Hand(Cardset):
    def __init__(self):
        self.cards = []
  
    def showcards(self):
        """shows cards in the hand"""
        for card in self.cards:
            print(card.__repr__())

    def isflush(self, cardvalues):
        suits = []
        for card in cardvalues:
            suits.append((str(card[-1:]), int(card[:-1])))

        sorted_suits = sorted(suits)
        card1, card2, card3 = sorted_suits[0:5], sorted_suits[1:6], sorted_suits[2:7]
        card_set = [card1, card2, card3]

        result = []
        for cards in card_set:
            if cards[0][0] == cards[-1][0]:
                result.append(cards[-1][1])

        result = sorted(result, reverse=True)
        if result:
            return (True, result[0])
        else:
            return (False, 0)


    def isstraight(self, cardvalues):
        values = []
        for card in cardvalues:
            values.append(int(card[:-1]))

        sorted_values = sorted(values)
        card1, card2, card3 = sorted_values[0:5], sorted_values[1:6], sorted_values[2:7]
        card_set = [card1, card2, card3]

        result = []
        for cards in card_set:
            if cards[1] == cards[0] + 1:
                if cards[2] == cards[1] + 1:
                    if cards[3] == cards[2] + 1:
                        if cards[4] == cards[3] + 1:
                            result.append(cards[-1])

        result = sorted(result, reverse=True)
        if result:
            return (True, result[0])
        else:
            return (False, 0)


    def isstraightflush(self, cardvalues):
        suits = []
        for card in cardvalues:
            suits.append((str(card[-1:]), int(card[:-1])))

        sorted_suits = sorted(suits)
        card1, card2, card3 = sorted_suits[0:5], sorted_suits[1:6], sorted_suits[2:7]
        card_set = [card1, card2, card3]

        results = []
        for cards in card_set:
            if cards[0][0] == cards[-1][0]:
                results.append((cards[-1][1], cards[0][1]))

        correct_results = []
        for result in results:
            if result[0] == result[1] + 4:
                correct_results.append(result[0])

        correct_results = sorted(correct_results, reverse=True)
        if correct_results:
            return (True, correct_results[0])
        else:
            return (False, 0)


    def ispair(self,cardvalues):
        sorted_cards = sorted(cardvalues)
        for card in sorted_cards:
            card = card[:-1]

        pair_vals = []
        for i in range(0,len(sorted_cards)-1):
            card1 = sorted_cards[i]
            card2 = sorted_cards[i+1]
            if card1[:-1] == card2[:-1]:
                pair_vals.append(card1[:-1])

        if len(pair_vals) != 0:
            return (True, pair_vals)
        else:
            return (False, pair_vals)

    def isthree(self, cardvalues):
        check = self.ispair(cardvalues)
        if check[0]:
            pairs = check[1]
            if len(pairs) >= 2:
                for i in range(0, len(pairs)-1):
                    if pairs[i] == pairs[i+1]:
                        return ("three", pairs[i])

    def isfour(self, cardvalues):
        check = self.ispair(cardvalues)
        if check[0]:
            pairs = check[1]
            if len(pairs) >= 3:
                for i in range(0, len(pairs)-2):
                    if (pairs[i] == pairs[i+1]) and (pairs[i+1] == pairs[i+2]):
                        return ("four", pairs[i])

    def isdoublepair(self,cardvalues):
        check = self.ispair(cardvalues)
        if check[0]:
            pairs = check[1]
            if len(pairs) == 2:
                if pairs[0] != pairs[1]:
                    if int(pairs[0]) > int(pairs[1]):
                        return ("two pair", pairs[0])
                    else:
                        return ("two pair", pairs[1])

    def isfullhouse(self, cardvalues):
        three_check = self.isthree(cardvalues)
        if three_check:
            pairs = self.ispair(cardvalues)
            #remove three from pair check
            if len(pairs[1])>2:
                return ('f_hs', three_check[1])


    def highcard(self,cardvalues):
        values = []
        for card in cardvalues:
            values.append(int(card[:-1]))

        sorted_values = sorted(values, reverse=True)
        return sorted_values[0]


    def playerhands(self):
        """Counts the number of each card in the hand
        puts results in a dict. """
        cardvalues = self.cards

        #some mapping function here
        string_values = ["2","3","4","5","6","7","8","9","T","J","Q", "K", "A"]
        values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        value_map = dict(zip(string_values,values))

        hand_keys = ["strt flsh", "four", "f_hs", "flsh", "strt", "three", "two pair", "pair", "high"]

        #run dictionary
        new_list = []
        for c in cardvalues:
            print(c)
            c = str(c)
            new_card = str(value_map[c[:1]])+str(c[-1:])
            new_list.append(new_card)

        #check for straight flush
        check = self.isstraightflush(new_list)
        if check[0]:
            return("strt flsh", check[1])

        #checks for 4 of a kind
        check = self.isfour(new_list)
        if check:
            return check

        #checks for full house
        check = self.isfullhouse(new_list)
        if check:
            return check

        #checks for flush
        check = self.isflush(new_list)
        if check[0]:
            return ("flsh", check[1])

        #checks for straight
        check = self.isstraight(new_list)
        if check[0]:
            return("strt", check[1])

        #checks for 3 of a kind, and 2 pairs
        check = self.isthree(new_list)
        if check:
            return check

        #checks for 2 pairs
        check = self.isdoublepair(new_list)
        if check:
            return check

        #checks for pair
        check = self.ispair(new_list)
        if check[0]:
            pair = check[1]
            return("pair", pair[0])

        #checks high card
        return ("high", self.highcard(new_list))
    def score_hand(self, points):
        hand_keys = ["strt flsh", "four", "f_hs", "flsh", "strt", "three", "two pair", "pair", "high"]
        values = [240,210,180,150,120,90,60,30,0]
        hand_map = dict(zip(hand_keys,values))

        type_score = str(points[0])
        s = int(hand_map[type_score])
        s += int(points[1])

        return s
    def tiebreaker(self):
        cardvalues = self.cards

        #some mapping function here
        string_values = ["2","3","4","5","6","7","8","9","T","J","Q", "K", "A"]
        values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        value_map = dict(zip(string_values,values))
        new_list = []
        for c in cardvalues:
            print(c)
            c = str(c)
            new_card = value_map[c[:1]]
            new_list.append(new_card)

        h = sorted(new_list)
        return h

class Deck(CardSet):
    def __init__(self):
        Suits = ["C", "D", "S", "H"]
        Values = ["2","3","4","5","6","7","8","9","T","J","Q", "K", "A"]

        self.cards = []
        for s in Suits:
            for v in Values:
                self.add(v,s)
        shuffle(self.cards)

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
        self.community_cards = Cardset()
        self.deck = Deck()
        self.table_pot = 0
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
    hand1 = Hand(pocket1.cards + communitycards.cards)
    score1 = hand1.score_hand(hand1.playerhands())
    
    hand2 = Hand(pocket2.cards + communitycards.cards)
    score2 = hand2.score_hand(hand2.playerhands())
    if score1 > score2:
        return "WIN"
    if score1 < score2:
        return "LOSS"
    else:
        return "DRAW"

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
