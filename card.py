from collections import * #frequwords
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
    def playerhands(self):
        """Counts the number of each card in the hand
        puts results in a dict. """
        cardvalues = defaultdict(int)
        havevalues = []
        handvalue = 100
        twookind = 0
        threeokind = 0
        fourokind = 0
        for card in self.cards:
            cardvalues[card.suit] += 1 #suit and value are swaped somwhere
        #checks for a streight
        #print (cardvalues)
        for i in range(len(cardvalues)-5):
            if i in cardvalues:
                if i+1 in cardvalues:
                    if i + 2 in cardvalues:
                        if i + 3 in cardvalues:
                            if i + 4 in cardvalues:
                                return(3)
        #looks for two and three of a kind
        for value in cardvalues:
            if cardvalues[value] == 3:
                threeokind = threeokind + 1
            if cardvalues[value] == 2:
                twookind = twookind + 1
            if cardvalues[value] == 4:
                fourokind = fourokind + 1

        if fourokind >= 1:
            return 1
        elif threeokind>=1 and twookind>=1: #full house
            return(2)
        elif threeokind >=1:
            return(4)
        elif twookind >= 2:
            return 5
        elif twookind >=1:
            return (6)
        else:
            return 100

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
        player1hands = self.player1.hand.playerhands()
        self.player2.hand.cards = self.player2.hand.cards + self.table.cards
    #   print (self.player2.hand.cards)
        player2hands = self.player2.hand.playerhands()
        print (player1hands)
        print (player2hands)
        if player1hands<player2hands:
            self.wins_Hand(self.player1)
        elif player2hands<player1hands:
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

