import random
from control import *
import pygame
from pygame.locals import *

def update_display(screen,game,buttons):

    buttons[0].draw()
    buttons[1].draw()
    buttons[2].draw()
    buttons[3].draw()

    [pocket1, pocket2, community_cards, money1, money2, table_pot] = get_game_status(game)
    #print(pocket1)
    #create cardback object which renders the same way a card does
    #back = 'purple_back'

    #render pocket cards in a way that makes sense
    for n in pocket1:
        n.draw()

    #render the community cards, but only if they exist
    #checks length of community cards
    #render appropriately

    #display monies
    #money1 = game.player1.funds
    #money2 = game.player2.funds
    #pot = game.table_pot

    #pygame.display.update()

def display_blank(screen):
    #displays starting screen, only called once
    pass
