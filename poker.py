"""
Create objects to handle modeling the game.
"""
import random
import pygame
from evaluatehand import *

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

class Button(pygame.sprite.Sprite):
    """Rudimentary card class to track suit and value"""
    def __init__(self, picture, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image =  pygame.image.load(picture).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.centerx = self.x + (self.image.get_width()/2)
        self.rect.centery = self.y + (self.image.get_height()/2)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

class Card(pygame.sprite.Sprite):
    """Rudimentary card class to track suit and value"""
    def __init__(self, value, suit, picture, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image =  pygame.image.load(picture).convert_alpha()
        self.image = pygame.transform.scale(self.image, (85, 130))
        self.image.set_colorkey(WHITE)
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
        """Returns the value and suit of a card"""
        return str(self.value)+str(self.suit)

class CardBack(pygame.sprite.Sprite):
    def __init__(self, picture, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image =  pygame.image.load(picture).convert_alpha()
        self.image = pygame.transform.scale(self.image, (85, 130))
        self.image.set_colorkey(WHITE)
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
        """Returns the value and suit of a card"""
        pass
    def add(self, card):
        """Adds an object to the hand"""
        self.cards.append(card)
    def remove(self, card):
        """Removes a specific card from the hand"""
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

    def makecardsets(self,cardvalues):
        suits = []
        values = []
        sorted_cards = sorted(cardvalues,key = lambda x: x[0])
        sorted_suits = sorted(cardvalues,key = lambda x: x[1])

        card1, card2, card3 = sorted_cards[0:5], sorted_cards[1:6], sorted_suits[2:7]
        card_set = [card1, card2, card3]
        return(card_set)

class Deck(CardSet):
    def __init__(self, screen):
        Suits = ["C", "D", "S", "H"]
        Values = ["2","3","4","5","6","7","8","9","T","J","Q", "K", "A"]

        self.cards = []
        for s in Suits:
            for v in Values:
                card_string = "./static/images/"+v+s+".png"
                card = Card(v,s,card_string, screen)
                self.add(card)
        random.shuffle(self.cards)

    def deal(self):
        """Returns the top card from the deck"""
        res = self.cards.pop()
        return res

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

    def bet(self, bet):
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

        # self.player1.blind_type == 'small'
        # self.player1.funds -= self.smallblind_amount
        # self.player2.funds -= self.bigblind_amount
        # self.player1.wager = self.smallblind_amount
        # self.player2.wager = self.bigblind_amount
        self.table_pot = 0;#self.player1.wager + self.player2.wager

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

def cardstolist(cardvalues):
    """Counts the number of each card in the hand
    puts results in a dict."""

    #some mapping function here
    string_values = ["2","3","4","5","6","7","8","9","T","J","Q", "K", "A"]
    values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    value_map = dict(zip(string_values,values))

    #run dictionary
    new_list = []
    for c in cardvalues:
        c_value = c.value
        c_suit = c.suit
        new_card = value_map[c_value]
        new_list.append([new_card,c_suit])

    return new_list

def compare_hands(pocket1, pocket2, community_cards):
   """
    Takes two pockets plus community cards and returns WIN, LOSS, or DRAW with respect to the first hand
   """
    p1hand = cardstolist(pocket1) + cardstolist(community_cards)
    p2hand = cardstolist(pocket2) + cardstolist(community_cards)

    score1 = scorehand(p1hand)
    score2 = scorehand(p2hand)
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
    else:
        high_card = pocket2[0]

    if high_card == 'A' : score = 10
    elif high_card == 'K' : score = 8
    elif high_card == 'Q' : score = 7
    elif high_card == 'J' : score = 6
    elif high_card == 'T' : score = 5
    else : score = int(high_card)/2
    # or use a table:
    #   card_scores = {'A': 10, 'K': 8, 'Q': 7, 'J': 6, 'T': 5}
    #   if high_card in card_scores:
    #     score = card_scores[high_card]
    #   else:
    #     score = int(high_card) / 2
    # or:
    #   score = card_scores[high_card] if high_card in card_scores else int(high_card) / 2
    # or:
    #   score = card_scores.get(high_card, None) or int(high_card) / 2

    # pairs
    is_pair = False
    if pocket1[0] == pocket2[0] :
        score = score * 2
        is_pair = True
    # or:
    #   is_pair = pocket1[0] == pocket2[0]
    #   if is_pair:
    #     score *= 2

    # suited
    if pocket1[1] == pocket2[1] : score += 2

    # gap
    gap = abs(value[pocket1[0]]-value[pocket2[0]])
    if gap == 1 : score += -1
    elif gap == 2 : score += -2
    elif gap == 3 : score += -4
    elif gap >= 4 : score += -5

    # correction
    if gap <= 1:
        if value[pocket1[0]] < value['Q'] and value[pocket2[0]] < value['Q']:
            score += 1

    # round up and return
    # does math.ceil do what you want here?
    return -(-score//1)

def deal(deck, cardset, quantity):
   """
    Removes the first 'quantity' cards from the deck and adds them to the cardset
   """
    for i in range(quantity):
        cardset.append(deck.deal())
