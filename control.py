"""
Run game and accept inputs. Could split document here.
"""
# import viewer
from poker import *

game = Game(False, False)
# initialize viewer
# viwer takes as input game and displays table

def get_input(player, other):
    """
    Get user or bot input.
    """
    money = 100                                                                 # change this to be user input

    if player.is_bot:                                                           # TODO: implement bot
        pass

    else:
        """ gets the move from the player"""
        move = input(player.name + ": check, call, raise, or fold?>>>")

    if move == "fold":
        player.fold()

    elif move == "raise": #player bets and abount
        player.call(other.wager)
        player.bet(money)

    elif move == "check":
        if player.wager != other.wager:
            print("You can't check. You haven't bet enough.")
            get_input(player, other)
        player.check()

    elif move == "call":
        if other.wager < player.wager:
            print("You can't call when you're ahead on betting!")
            get_input(player, other)
        if player.funds - money < 0:
            print("You don't have enough money. Sorry.")
            get_input(player, other)
        player.call(other.wager)

    else:
        print("Not a valid move - try again")
        get_input(player, other)

    return player.wager

def betting():
    """Players bet against each other"""
    game.player1.wager = get_input(game.player1, game.player2)
    print("Player 1:", game.player1.wager)
    print("Player 2:", game.player2.wager)
    if game.player1.folded:
        print("player1 folded")
        return False
    game.player2.wager = get_input(game.player2, game.player1)
    print("Player 1:", game.player1.wager)
    print("Player 2:", game.player2.wager)
    if game.player2.folded:
        print("player2 folded")
        return False

    if game.player1.wager == game.player2.wager:
        print("moving on")
        return True
    else:
        print("you're stuck in betting")
        return betting()

def newround():
    game.community_cards = []
    game.player1.pocket =[]
    game.player2.pocket =[]
    game.player1.folded = False
    game.player2.folded = False
    preflop()

def preflop():
    # deal
    deal(game.deck, game.player1.pocket, 2)
    deal(game.deck, game.player2.pocket, 2)
    print(game.player1.blind_type)
    print("Player 1:", game.player1.pocket)
    print("Player 2:", game.player2.pocket)
    # betting
    if betting():
    # advance to next round
        game.update_tablepot()
        flop()
    else:
        showdown()

def flop():
    # deal
    deal(game.deck, game.community_cards, 3)
    print("Player 1:", game.player1.pocket)
    print("Player 2:", game.player2.pocket)
    print("Community Cards:", game.community_cards)
    # betting
    if betting():
        # advance to next round
        game.update_tablepot()
        turn()
    else:
        showdown()

def turn():
    # deal
    deal(game.deck, game.community_cards, 1)
    print("Player 1:", game.player1.pocket)
    print("Player 2:", game.player2.pocket)
    print("Community Cards:", game.community_cards)
    # betting
    if betting():
        # advance to next round
        game.update_tablepot()
        river()
    else:
        showdown()

def river():
    # deal
    deal(game.deck, game.community_cards, 1)
    print("Player 1:", game.player1.pocket)
    print("Player 2:", game.player2.pocket)
    print("Community Cards:", game.community_cards)
    # betting
    betting()
    game.update_tablepot()
    showdown()

def showdown():
    """Finds Winner Gives Money"""
    # return winner
    print("Player 1:", game.player1.pocket)
    print("Player 2:", game.player2.pocket)
    print("Community Cards:", game.community_cards)
    if game.player1.folded:
        game.player2.funds += game.table_pot
    elif game.player2.folded:
        game.player1.funds += game.table_pot
    else:
        winner = compare_hands(game.player1.pocket, game.player2.pocket, game.community_cards)
        if winner == "Player1":
            game.player1.funds += game.table_pot
        elif winner == "Player2":
            game.player2.funds += game.table_pot
        else:
            game.player1.funds += game.table_pot/2
            game.player2.funds += game.table_pot/2

newround()
