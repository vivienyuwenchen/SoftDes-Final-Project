from model import *
import pygame
from pygame.locals import *
from poker import *

def update_display(screen,game,buttons):
    """ Updates display for game interaction """
    # display buttons
    for n in buttons:
        n.draw()

    # default card back image
    cardBack = CardBack('./static/images/purple_back.png', screen)

    # load updates from game
    [pocket1, pocket2, community_cards, money1, money2, table_pot] = get_game_status(game)

    # display player's pocket cards
    pocket1_pairs = [(540,250),(670,250)]
    for i in range(0, len(pocket1.cards)):
        n = pocket1.cards[i]
        n.x, n.y = pocket1_pairs[i]
        n.draw()

    # display opponent's pocket cards
    pocket2_pairs = [(40,250),(170,250)]
    for i in range(0, len(pocket2.cards)):
        n = cardBack
        n.x, n.y = pocket2_pairs[i]
        n.draw()

    # display community cards
    community_pairs = [(40,40), (170,40),(300,40),(430,40),(560,40)]
    table_length = len(community_cards)
    for i in range(0, table_length):
        n = community_cards[i]
        n.x, n.y = community_pairs[i]
        n.draw()

    # display table
    table_backs = 5-table_length
    new_pairs = community_pairs[table_length:]
    for i in range(0, table_backs):
        n = cardBack
        n.x, n.y = new_pairs[i]
        n.draw()

    # display monies
    font = pygame.font.SysFont("comicsansms", 20)
    money1_ = font.render("Your Money: " + str(money1), True, (255, 255, 255))
    screen.blit(money1_, (540, 220))
    money2_ = font.render("Opponent Money: " + str(money2), True, (255, 255, 255))
    screen.blit(money2_, (40, 220))
    table_pot_ = font.render("Table Pot: " + str(table_pot), True, (255, 255, 255))
    screen.blit(table_pot_, (300, 300))
