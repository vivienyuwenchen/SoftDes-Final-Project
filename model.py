from poker import *
from montecarlo import *
import view
import pygame,sys,inspect,random
from pygame.locals import *

def get_user_input(buttons):
    raise_button = buttons[0]
    check_button = buttons[1]
    call_button = buttons[2]
    fold_button = buttons[3]

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if raise_button.rect.collidepoint(event.pos):
                act = "raise"
            elif call_button.rect.collidepoint(event.pos):
                act = "call"
            if check_button.rect.collidepoint(event.pos):
                act = "check"
            if fold_button.rect.collidepoint(event.pos):
                act = "fold"
    try:
        return act
    except:
        pass

def get_bot_input(episode,game,player):
    """gets move from bot and updates trainer"""
    act = mc_control_epsilon_greedy(episode, game, player)
    return act

def get_game_status(game):
    return [game.player1.pocket, game.player2.pocket, game.community_cards.cards, game.player1.funds, game.player2.funds, game.table_pot]

def process_user_input(game, player, other, buttons):
    """
    Get user or bot input.
    """
    money = 100

    move = get_user_input(buttons)
    if move:
        print(move)
        print(player.wager)
        print(other.wager)
        if move == "fold":
            player.fold()

        elif move == "raise": #player bets an amount
            player.call(other.wager)
            player.bet(money)

        elif move == "check" or move == "call" or move == "match":
            if player.funds - money < 0:
                print("You don't have enough money. Sorry")
                process_user_input(game, player, other, buttons)
            if other.wager < player.wager:
                print("You can't match when you're ahead on betting!")
                process_user_input(game, player, other, buttons)
            player.call(other.wager)
            player.check()

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
            if player.funds - money < 0:
                print("You don't have enough money. Sorry")
                process_bot_input(game,player,other,episode)
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
            player.check()
        return player.wager
    else:
        pass

def betting(game, episode, buttons):
    """Players bet against each other"""
    potential_wager = process_user_input(game, game.player1, game.player2, buttons)

    if potential_wager:
        game.player1.wager = potential_wager
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
    game.community_cards.cards = []
    # deal
    game.player1.pocket.cards = []
    game.player2.pocket.cards = []
    game.new_deck()
    deal(game.deck, game.player1.pocket.cards, 2)
    deal(game.deck, game.player2.pocket.cards, 2)
    game.player1.folded = False
    game.player2.folded = False
    game.table_pot = 0
    

def preflop(game, episode, buttons):
    check_status = betting(game, episode, buttons)
    return check_status

def flop(game, episode, buttons, run_status):
    # deal
    if run_status == 'go':
        deal(game.deck, game.community_cards.cards, 3)
        print("Player 1:", game.player1.pocket.cards)
        print("Player 2:", game.player2.pocket.cards)
        print("Community Cards:", game.community_cards.cards)

    check_status = betting(game, episode, buttons)
    return check_status

def turn(game, episode, buttons, run_status):
    if run_status == 'go':
        deal(game.deck, game.community_cards.cards, 1)
        print("Player 1:", game.player1.pocket.cards)
        print("Player 2:", game.player2.pocket.cards)
        print("Community Cards:", game.community_cards.cards)

    check_status = betting(game, episode, buttons)
    return check_status

def river(game, episode, buttons, run_status):
    if run_status == 'go':
        deal(game.deck, game.community_cards.cards, 1)
        print("Player 1:", game.player1.pocket.cards)
        print("Player 2:", game.player2.pocket.cards)
        print("Community Cards:", game.community_cards.cards)

    check_status = betting(game, episode, buttons)
    return check_status

def showdown(game, episode):
    """Finds Winner Gives Money"""
    # return winner
    print("Player 1:", game.player1.pocket.cards)
    print("Player 2:", game.player2.pocket.cards)
    print("Community Cards:", game.community_cards.cards)

    if game.player1.folded:
        game.winner = "Player2"
        game.player2.funds += game.table_pot
    elif game.player2.folded:
        game.winner = "Player1"
        game.player1.funds += game.table_pot
    else:
        winner = compare_hands(game.player1.pocket.cards, game.player2.pocket.cards, game.community_cards.cards)
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

    mc_control_epsilon_greedy(episode, game, game.player1)
    mc_control_epsilon_greedy(episode, game, game.player2)
    print("Winner:", game.winner)
    print("Player 1:", game.player1.funds)
    print("Player2:", game.player2.funds)
    print("Game Over")
    print("New Round")

def update_game(game, episode, buttons,run_status):
    """
    Do the appropriate action to the game, increase table pot,
    check if they folded, etc
    As always, folded skips straight to the showdown round
    Else, generate a bot input, and change the game accordingly
    Folded skips to showdown
    """

    game_round = game.round
    if game_round == 'newround':
        newround(game)
        print(game_round)
        game.round = 'preflop'
        print(game.round)
        return 'go'
    elif game_round == 'preflop':
        check = preflop(game, episode, buttons)
        if check == True:
            game.round = 'flop'
            return 'go'
        elif check == False:
            game.round = 'showdown'
            print(game.round)
            return 'go'
        elif check == 'no input':
            game.round = 'preflop'
            return 'stop'
        return 'stop'
    elif game_round == 'flop':
        check = flop(game, episode, buttons, run_status)
        if check == True:
            game.round = 'turn'
            return 'go'
        elif check == False:
            game.round = 'showdown'
            return 'go'
        elif check == 'no input':
            game.round = 'flop'
            return 'stop'
        return 'stop'
        pass
    elif game_round == 'turn':
        check = turn(game, episode, buttons, run_status)
        if check == True:
            game.round = 'river'
            return 'go'
        elif check == False:
            game.round = 'showdown'
            return 'go'
        elif check == 'no input':
            game.round = 'turn'
            return 'stop'
        return 'stop'
    elif game_round == 'river':
        check = turn(game, episode, buttons, run_status)
        if check == True:
            game.round = 'showdown'
            return 'go'
        elif check == False:
            game.round = 'showdown'
            return 'go'
        elif check == 'no input':
            game.round = 'river'
            return 'stop'
        return 'stop'
    elif game_round == 'showdown':
        showdown(game, episode)
        game.round = 'newround'
        return 'go'
    pass
