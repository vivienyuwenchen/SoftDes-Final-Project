import random
from control import *
from model import *
import pygame
from pygame.locals import *
from poker import *

def update_display(screen,game,buttons):

    buttons[0].draw()
    buttons[1].draw()
    buttons[2].draw()
    buttons[3].draw()

    cardBack = CardBack('./static/images/purple_back.png', screen)

    [pocket1, pocket2, community_cards, money1, money2, table_pot] = get_game_status(game)

    pocket1_pairs = [(540,250),(670,250)]
    for i in range(0, len(pocket1.cards)):
        n = pocket1.cards[i]
        n.x, n.y = pocket1_pairs[i]
        n.draw()

    pocket2_pairs = [(40,250),(170,250)]
    for i in range(0, len(pocket2.cards)):
        n = cardBack
        n.x, n.y = pocket2_pairs[i]
        n.draw()

    #render the community cards, but only if they exist
    #checks length of community cards
    #render appropriately

    community_pairs = [(40,40), (170,40),(300,40),(430,40),(560,40)]
    table_length = len(community_cards)
    for i in range(0, table_length):
        n = community_cards[i]
        n.x, n.y = community_pairs[i]
        n.draw()

    table_backs = 5-table_length
    new_pairs = community_pairs[table_length:]
    for i in range(0, table_backs):
        n = cardBack
        n.x, n.y = new_pairs[i]
        n.draw()

    #display monies
    #money1 = game.player1.funds
    #money2 = game.player2.funds
    #pot = game.table_pot

    #pygame.display.update()

def display_blank(screen):
    #displays starting screen, only called once
    pass
