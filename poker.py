"""
Create objects to handle modeling the game.
"""
import random
import pygame

white = (255, 255, 255)
green = (0, 255, 0)

class Button(pygame.sprite.Sprite):
    """ Rudimentary card class to track suit and value """
    def __init__(self, picture, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image =  pygame.image.load(picture).convert_alpha()
        self.image.set_colorkey(white)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.centerx = self.x + (self.image.get_width()/2)
        self.rect.centery = self.y + (self.image.get_height()/2)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

class Card(pygame.sprite.Sprite):
    """ Rudimentary card class to track suit and value """
    def __init__(self, value, suit, picture, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image =  pygame.image.load(picture).convert_alpha()
        self.image = pygame.transform.scale(self.image, (85, 130))
        self.image.set_colorkey(white)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.x = 600
        self.y = 450

        self.rect.centerx = self.x + (self.image.get_width()/2)
        self.rect.centery = self.y + (self.image.get_height()/2)

        self.suit = suit
        self.value = value

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def __repr__(self):
        """ Returns the value and suit of a card"""
        return str(self.value)+str(self.suit)
class CardBack(pygame.sprite.Sprite):
    def __init__(self, picture, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image =  pygame.image.load(picture).convert_alpha()
        self.image = pygame.transform.scale(self.image, (85, 130))
        self.image.set_colorkey(white)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.x = 600
        self.y = 450

        self.rect.centerx = self.x + (self.image.get_width()/2)
        self.rect.centery = self.y + (self.image.get_height()/2)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

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
class Hand(CardSet):
    def __init__(self, cards):
        self.cards = cards

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
        values = []
        sorted_cards = sorted(cardvalues,key = lambda x: x[0])
        print (sorted_cards)

        sorted_suits = sorted(suits)
        card1, card2, card3 = sorted_suits[0:5], sorted_suits[1:6], sorted_suits[2:7]
        card_set = [card1, card2, card3]

        results = []
        for cards in card_set:
            for i in range(len(cards)-1):

                if cards[i][1] != cards[i+1][1]:
                    results

                if cards[i][0] != cards[i+1][0]-1:
                        return False


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


    def player_hands(self):
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
            c_value = c.value
            c_suit = c.suit
            new_card = value_map[c_value]
            new_list.append([new_card,c_suit])


        #check for straight flush
        print(new_list)
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
    def __init__(self, screen):
        Suits = ["C", "D", "S", "H"]
        Values = ["2","3","4","5","6","7","8","9","T","J","Q", "K", "A"]

        self.cards = []
        for s in Suits:
            for v in Values:
                #self.add((v,s))
                card_string = "./static/images/"+v+s+".png"
                card = Card(v,s,card_string, screen)
                self.add(card)
        random.shuffle(self.cards)

    def deal(self):
        """Returns the top card from the deck"""
        return self.cards.pop()
class Player():
    def __init__(self,funds, name, is_bot, isturn):
        self.pocket = CardSet()
        self.funds = funds
        self.isturn = isturn
        self.folded = False
        self.wager = 0
        self.name = name
        self.is_bot = is_bot
        self.blind_type = 'small'
        self.move = ''

    def check(self):
        self.isturn = False
        pass
    def fold(self):
        self.folded = True
        pass
    def bet (self, bet):
        self.wager += bet
        self.funds -= bet
        self.isturn = False
        pass
    def call(self, wager2):
        """player matches other player's bet"""
        bet = wager2-self.wager
        self.funds -= bet
        self.wager = wager2
        self.isturn = False

class Game():
    def __init__(self, is_bot1, is_bot2, screen):
        self.round = 'newround'
        self.community_cards = CardSet()
        self.deck = Deck(screen)
        self.smallblind_amount = 50
        self.bigblind_amount = 100
        self.player1 = Player(3000, "Player1", is_bot1, True)
        self.player2 = Player(3000, "Player2", is_bot2, False)
        self.winner = ''

        self.screen = screen

        self.player1.blind_type == 'small'
        self.player1.funds -= self.smallblind_amount
        self.player2.funds -= self.bigblind_amount
        self.player1.wager = self.smallblind_amount
        self.player2.wager = self.bigblind_amount
        self.table_pot = self.player1.wager + self.player2.wager
    def new_deck(self):
        self.deck = Deck(self.screen)

    def __repr__(self):
        print("Table Cards: " + str(self.community_cards))
        print("Table Pot: " + str(self.table_pot.value))
        print("Player 1 Pocket: " + str(self.player1.hand.cards))
        print("Player1 Chips: " + str(self.player1.pot.value))
        print("Player 2 Pocket: " + str(self.player2.hand.cards))
        print("Player2 Chips: " + str(self.player2.pot.value))

    def update_tablepot(self):
        self.table_pot = self.player1.wager + self.player2.wager

def compare_hands(pocket1, pocket2, community_cards):
    """
    Takes two pockets plus community cards and returns WIN, LOSS, or DRAW with respect to the first hand
    """
    cards1 = pocket1
    hand1 = Hand(pocket1 + community_cards)
    score1 = hand1.score_hand(hand1.player_hands())

    hand2 = Hand(pocket2 + community_cards)
    score2 = hand2.score_hand(hand2.player_hands())
    if score1 > score2:
        return "Player1"
    if score1 < score2:
        return "Player2"
    else:
        return "Draw"


def hand_strength(pocket1, pocket2):
    """
    Takes a pocket and the community cards and returns the probability of winning the hand [0:1]
    Returns the Chen formula hand strength for two cards.
    card = (str : suit, str : rank)
    rank : 2,3,4,5,6,7,8,9,10,J,Q,K,A
    suit : s,h,c,d
    """
    score = 0
    value = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

    pocket1 = pocket1.__repr__()
    pocket2 = pocket2.__repr__()

	#high card
    if value[pocket1[0]] > value[pocket2[0]]:
        high_card = pocket1[0]
    else : high_card = pocket2[0]

    if high_card == 'A' : score = 10
    elif high_card == 'K' : score = 8
    elif high_card == 'Q' : score = 7
    elif high_card == 'J' : score = 6
    elif high_card == 'T' : score = 5
    else : score = int(high_card)/2

    #pairs
    is_pair = False
    if pocket1[0] == pocket2[0] :
        score = score * 2
        is_pair = True

    #suited
    if pocket1[1] == pocket2[1] : score += 2

    #gap
    gap = abs(value[pocket1[0]]-value[pocket2[0]])
    if gap == 1 : score += -1
    elif gap == 2 : score += -2
    elif gap == 3 : score += -4
    elif gap >= 4 : score += -5

    #correction
    if gap <= 1:
        if value[pocket1[0]] < value['Q'] and value[pocket2[0]] < value['Q']:
            score += 1

    #round up and return
    return -(-score//1)

def deal(deck, cardset, quantity):
    """
    Removes the first 'quantity' cards from the deck and adds them to the cardset
    """
    for i in range(quantity):
        cardset.append(deck.deal())
