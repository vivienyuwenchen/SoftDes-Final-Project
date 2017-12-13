"""
Run to train bot and/or play from command line.
"""
from poker import *
from montecarlo import *

def get_input(player, other):
    """
    Get user or bot input.
    """
    money = 100                                                                 # change this to be user input

    if player.is_bot:
        """gets move from bot and updates trainer"""
        move = mc_control_epsilon_greedy(episode, game, player)
        print(player.name,":", move)

    else:
        """ gets the move from the player"""
        move = input(player.name + ": check, call, raise, or fold?>>>")

    if move == "fold":
        player.fold()

    elif move == "raise": #player bets and amount
        if player.funds - money < 0:
            print("You don't have enough money. Sorry")
            get_input(player, other)
        player.call(other.wager)
        player.bet(money)

    elif move == "check" or move == "call" or move == "match":
        if player.funds - money < 0:
            print("You don't have enough money. Sorry")
            get_input(player, other)
        if other.wager < player.wager:
            print("You can't match when you're ahead on betting!")
            get_input(player, other)
        player.call(other.wager)
        #player.check()

    else:
        print("Not a valid move - try again")
        get_input(player, other)

    return player.wager

def betting():
    """Players bet against each other"""
    game.player1.wager = get_input(game.player1, game.player2)
    print("Player 1:", game.player1.wager)
    print("Player 2:", game.player2.wager)

    game.update_tablepot()

    if game.player1.folded:
        print("player1 folded")
        return False

    game.player2.wager = get_input(game.player2, game.player1)
    print("Player 1:", game.player1.wager)
    print("Player 2:", game.player2.wager)

    game.update_tablepot()

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
    # deal
    game.player1.pocket = []
    game.player2.pocket = []
    deal(game.deck, game.player1.pocket, 2)
    deal(game.deck, game.player2.pocket, 2)
    game.player1.folded = False
    game.player2.folded = False

    preflop()

def preflop():
    print(game.player1.blind_type)
    print("Player 1:", game.player1.pocket)
    print("Player 2:", game.player2.pocket)

    # betting
    if betting():
    # advance to next round
        game.round = 2
        flop()
    else:
        game.round = 5
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
        game.round = 3
        turn()
    else:
        game.round = 5
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
        game.round = 4
        river()
    else:
        game.round = 5
        showdown()

def river():
    # deal
    deal(game.deck, game.community_cards, 1)
    print("Player 1:", game.player1.pocket)
    print("Player 2:", game.player2.pocket)
    print("Community Cards:", game.community_cards)

    # betting
    betting()
    game.round = 5
    showdown()

def showdown():
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

    mc_control_epsilon_greedy(episode, game, game.player1)
    mc_control_epsilon_greedy(episode, game, game.player2)
    print("Winner:", game.winner)
    print("Player 1:", game.player1.funds)
    print("Player2:", game.player2.funds)
    print("Game Over")

if __name__ == "__main__":
    for i in range(10):
        # create new episode for training with every new game
        episode = []
        game = Game(False, True)
        newround()
