from collections import * #frequwords
from random import*
class Card():
    """ Rudimentary card class to track suit and value """
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
    def __repr__(self):
        """ Returns the value and suit of a card"""
        return str(self.value)+str(self.suit)
        #return("(%r %r)" % (  (self.suit),(self.value)))

class Deck():
    def __init__(self):
        self.cards = []
    def createDeck(self):
        Suits = ["C", "D", "S", "H"]
        Values = ["2","3","4","5","6","7","8","9","T","J","Q", "K", "A"]

        for s in Suits:
            for v in Values:
                self.add(v,s)
        shuffle(self.cards)
    def add(self, value, suit):
        """Adds a card of value num and suit suit to the
        deck"""
        self.cards.append(Card(value,suit))

    def addcard(self, thiscard):
        """Adds an object to the deck"""
        self.cards.append(thiscard)

    def showcards(self):
        """Shows all of the cards in the deck"""
        for card in self.cards:
            print(card.__repr__())
    #def shuffle_deck(self):
        """Shuffles the deck"""
    #   random.shuffle(self.cards)

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

class Pot():
    def __init__(self, money):
        self.value = money

    def __repr__(self):
        return self.value

class Player():
    def __init__(self,money, name):
        self.hand = Hand()
        self.pot = Pot(money)
        self.isturn = False
        self.folded = False
        self.bigblind = False
        self.smallblind = False
        self.contribution = 0
        self.name = name
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
        self.contribution += raise_money
        reciverpot.value += raise_money
        self.isturn = False


    def player_call(self,call):
        """player matches other player's bet"""
        other.money_to_pot(call, self.pot)
        self.isturn = False

        pass
class Game():
    def __repr__(self):
        print("Table Cards: " + str(self.table.cards))
        print("table Pot: " + str(self.tablepot.value))
        print("Player 1 Pocket: " + str(self.player1.hand.cards))
        print("Player1 Chips: " + str(self.player1.pot.value))
        print("Player 2 Pocket: " + str(self.player2.hand.cards))
        print("Player2 Chips: " + str(self.player2.pot.value))
        print()
    def __init__(self, money1, money2):
        self.table = Hand()
        self.deck = Deck()
        self.deck.createDeck()

        self.tablepot = Pot(0)
        self.player1_contribution = 0
        self.player2_contribution = 0
        self.smallblind_ammount = 50
        self.bigblind_ammount = 100
        self.player1 = Player(money1, "one")
        self.player2 = Player(money2, "two")

    def add_deck(self):
        """Adds another deck if the first one runs low"""
        self.newdeck = Deck()
        self.newdeck.createDeck()
        self.deck.cards = self.deck.cards+self.newdeck.cards

    def pocket(self):
        """deals each player 2 cards"""
        self.player1.hand.add(self.deck.deal())
        self.player2.hand.add(self.deck.deal())
        self.player1.hand.add(self.deck.deal())
        self.player2.hand.add(self.deck.deal())

        self.blinds(self.player1,self.player2)
        self.__repr__()
        self.player1.isturn = True
        self.player2.isturn = True
        #Print(player2.folded)
        while self.player1.isturn == True or self.player2.isturn == True:
            if self.player1.isturn == True:
                self.player_move(self.player1,self.player2)
            if self.player2.isturn == True:
                self.player_move(self.player2,self.player1)
                print("player 1 tern: " + str(self.player1.isturn))
                print("player 2 tern: " + str(self.player2.isturn))


    def flop(self):
        self.table.add(self.deck.deal())
        self.table.add(self.deck.deal())
        self.table.add(self.deck.deal())
        self.__repr__()
        self.player1.isturn = True
        self.player2.isturn = True
        while self.player1.isturn == True or self.player2.isturn == True:
            if self.player1.isturn == True:
                self.player_move(self.player1,self.player2)
            if self.player2.isturn == True:
                self.player_move(self.player2,self.player1)

        """puts three cards on the table"""


    def turn(self):
        """puts one card on the table"""
        self.table.add(self.deck.deal())
        self.__repr__()
        self.player1.isturn = True
        self.player2.isturn = True
        while self.player1.isturn == True or self.player2.isturn == True:
            if self.player1.isturn == True:
                self.player_move(self.player1,self.player2)
            if self.player2.isturn == True:
                self.player_move(self.player2,self.player1)
        pass

    def river(self):
        """puts one card on the table"""
        self.table.add(self.deck.deal())
        self.__repr__()
        self.player1.isturn = True
        self.player2.isturn = True
        while self.player1.isturn == True or self.player2.isturn == True:
            if self.player1.isturn == True:
                self.player_move(self.player1,self.player2)
            if self.player2.isturn == True:
                self.player_move(self.player2,self.player1)
        pass

    def showdown(self):
        """Finds Winner Gives Money"""
        self.player1.hand.cards = self.player1.hand.cards + self.table.cards
    #   print (self.player1.hand.cards)
        points1 = self.player1.hand.playerhands()
        print(points1)
        player1hands = self.player1.hand.score_hand(points1)
        print(player1hands)
        self.player2.hand.cards = self.player2.hand.cards + self.table.cards
    #   print (self.player2.hand.cards)
        points2 = self.player2.hand.playerhands()
        print(points2)
        player2hands = self.player2.hand.score_hand(points2)
        print(player2hands)
        if player1hands>player2hands:
            self.wins_Hand(self.player1)
        elif player2hands>player1hands:
            self.wins_Hand(self.player2)
        else:
            self.draw()
        print("Next Round")

    def wins_Hand(self,player):
        print("Winner: " + player.name)
        player.pot.value += self.tablepot.value
        self.tablepot.value = 0
        print(self.player1.name + str(self.player1.pot.value))
        print(self.player2.name + str(self.player2.pot.value))
        print("------------")

    def draw(self):
        print("draw")
        self.player1.pot.value += self.tablepot.value/2
        self.player2.pot.value += self.tablepot.value/2
        self.tablepot.value = 0
        print(str(self.player1.pot.value))
        print(str(self.player2.pot.value))


#   def counts_player_contrib(self,player, money, the_pot):
        """ when ever a player adds money to the table
        Pot add that money to the players pot contibution
        #>>> player1 = Player(1000)

        #>>> pot = Pot(100)

        #>>> Game.counts_player_contrib(player1, 100, pot)
        #100

        """

#       player.player_bet(money,the_pot)
#       player.player_contribute(money)
#       (player.player_showContribution())

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
        move = input(player.name + ": check, raise, or fold?>>>")
        if move == "fold":
            player.folded = True   #player folds
            player.isturn = False
            other.isturn = False


        elif move == move:
            #player maches the cotrobution of the other player

            if player.contribution < other.contribution:
                money = other.contribution - player.contribution
                self.__repr__()
                player.player_bet(money, self.tablepot)
            player.isturn = False


        elif move == "raise": #player bets and abount
            money = 100
            player.player_bet(money, self.tablepot)
            self.__repr__()
            player.isturn = False
            other.isturn = True
        else:
            print("input error try again")
            self.player_move(self.player1,self.player2)
    def newround(self):
        self.table.cards = []
        self.player1.hand.cards =[]
        self.player2.hand.cards =[]
        self.player1.folded = False
        self.player2.folded = False


            #do nothing

#if __name__ == "__main__":
   # import doctest
#    doctest.testmod()
   # doctest.run_docstring_examples(Game.counts_player_contrib, globals(),verbose=True)
