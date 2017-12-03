import random
import control
import pygame

def display(game):

    pocket1 = game.player1.pocket
    pocket2 = game.player2.pocket
    community_cards = game.community_cards

    #create cardback object which renders the same way a card does
    #back = 'purple_back'

    #render pocket cards in a way that makes sense
    pocket1[0].draw()

    #render the community cards, but only if they exist
    #checks length of community cards
    #render appropriately

    #display monies
    money1 = game.player1.funds
    money2 = game.player2.funds
    pot = game.table_pot



def display_blank():
    #displays starting screen, only called once
    pass
