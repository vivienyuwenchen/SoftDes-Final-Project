from poker import *
from montecarlo import *
import view
import pygame,sys,inspect,random
from pygame.locals import *
import control

def get_bot_input(episode,game,player):
    """gets move from bot and updates trainer"""
    act = mc_control_epsilon_greedy(episode, game, player)
    return act

def get_game_status(game):
    return [game.player1.pocket, game.player2.pocket, game.community_cards, game.player1.funds, game.player2.funds, game.table_pot]

def process_user_input(game, player, other, buttons):
    """
    Get user or bot input.
    """
    money = 100

    move =  control.get_user_input(buttons)
    if move:
        if move == "fold":
            player.fold

        elif move == "raise": #player bets an amount
            player.call(other.wager)
            player.bet(money)

        elif move == "check":
            if player.wager != other.wager:
                print("You can't check. You haven't bet enough.")
                process_input(game, player, other)
            player.check()

        elif move == "call":
            if other.wager < player.wager:
                print("You can't call when you're ahead on betting!")
                process_input(game, player, other)
            if player.funds - money < 0:
                print("You don't have enough money. Sorry.")
                process_input(game, player, other)
            player.call(other.wager)
        return player.wager
    else:
        pass

def process_bot_input(game, player, other, episode):
    """
    Get user or bot input.
    """
    money = 100

    move =  get_bot_input(episode,game,player)
    if move:
        if move == "fold":
            player.fold()

        elif move == "raise": #player bets an amount
            player.call(other.wager)
            player.bet(money)

        elif move == "check":
            if player.wager != other.wager:
                print("You can't check. You haven't bet enough.")
                process_input(game, player, other)
            player.check()

        elif move == "call":
            if other.wager < player.wager:
                print("You can't call when you're ahead on betting!")
                process_input(game, player, other)
            if player.funds - money < 0:
                print("You don't have enough money. Sorry.")
                process_input(game, player, other)
            player.call(other.wager)
        return player.wager
    else:
        pass

def betting(game, episode, buttons):
    """Players bet against each other"""
    game.player1.wager = process_user_input(game, game.player1, game.player2, buttons)

    if game.player1.wager:
        game.update_tablepot()

        if game.player1.folded:
            print("player1 folded")
            return False

        game.player2.wager = process_bot_input(game, game.player2, game.player1, episode)
        game.update_tablepot()

        if game.player2.folded:
            print("player2 folded")
            return False

        if game.player1.wager == game.player2.wager:
            print("moving on")
            return True
        else:
            print("you're stuck in betting")
            return betting
    else:
        return 'no input'

def newround(game):
    game.community_cards = []
    # deal
    game.player1.pocket.cards = []
    game.player2.pocket.cards = []
    deal(game.deck, game.player1.pocket.cards, 2)
    deal(game.deck, game.player2.pocket.cards, 2)
    game.player1.folded = False
    game.player2.folded = False

def preflop(game, episode, buttons):
    check_status = betting(game, episode, buttons)
    return check_status

def flop(game):
    # deal
    deal(game.deck, game.community_cards, 3)
    print("Player 1:", game.player1.pocket)
    print("Player 2:", game.player2.pocket)
    print("Community Cards:", game.community_cards)

def turn(game):
    # deal
    deal(game.deck, game.community_cards, 1)
    print("Player 1:", game.player1.pocket)
    print("Player 2:", game.player2.pocket)
    print("Community Cards:", game.community_cards)

def river(game):
    # deal
    deal(game.deck, game.community_cards, 1)
    print("Player 1:", game.player1.pocket)
    print("Player 2:", game.player2.pocket)
    print("Community Cards:", game.community_cards)

def showdown(game):
    """Finds Winner Gives Money"""
    # return winner
    print("Player 1:", game.player1.pocket)
    print("Player 2:", game.player2.pocket)
    print("Community Cards:", game.community_cards)

    if game.player1.folded:
        game.winner = "Player2"
        game.player2.funds += game.table_pot
    elif game.player2.folded:
        game.winner = "Player1"
        game.player1.funds += game.table_pot
    else:
        winner = compare_hands(game.player1.pocket, game.player2.pocket, game.community_cards)
        if winner == "Player1":
            game.winner = "Player1"
            game.player1.funds += game.table_pot
        elif winner == "Player2":
            game.winner = "Player2"
            game.player2.funds += game.table_pot
        else:
            game.winner = "Tie"
            game.player1.funds += game.table_pot/2
            game.player2.funds += game.table_pot/2

    print("Winner:", game.winner)
    print("Player 1:", game.player1.funds)
    print("Player2:", game.player2.funds)
    print("Game Over")

def update_game(game, episode, buttons):
    """
    We know that input is going to be user input
    We need this program to go to the correct stage of the game, depending
    on what was happening before
    We want to do the appropriate action to the game, increase table pot,
    check if they folded, etc
    As always, folded skips straight to the showdown round
    Else, generate a bot input, and change the game accordingly
    Folded skips to showdown
    game needs new attribute 'round'
    """
    game_round = game.round
    if game_round == 'newround':
        newround(game)
        game.round = 'preflop'
        pass
    elif game_round == 'preflop':
        check = preflop(game, episode, buttons)
        if check == True:
            game.round = 'flop'
        elif check == False:
            game.round = 'showdown'
        elif check == 'no input':
            game.round = preflop
        pass
    elif game_round == 'flop':
        smthng
        game.round = 'turn'
        pass
    elif game_round == 'turn':
        smthng
        game.round = 'river'
        pass
    elif game_round == 'river':
        smthng
        game.round = 'showdown'
        pass
    elif game_round == 'showdown':
        smthng
        game.round = 'newround'
        pass

    print("Something went wrong, dumbass")
    pass
