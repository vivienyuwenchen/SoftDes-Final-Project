"""
Run game and accept inputs. Could split document here.
"""
# import viewer

game = Game()
# initialize viewer
# viwer takes as input game and displays table

def get_input(player, other):
    """
    Get user or bot input.
    """
    if player.is_bot:                                                           # TODO: implement bot
        pass
    else:
        """ gets the move from the player"""
        move = input(player.name + ": check, call, raise, or fold?>>>")

    if move == "fold":
        player.fold

    elif move == "raise": #player bets and abount
        player.call(other.wager)
        money = 100                                                             # change this to be user input
        player.bet(money)

    elif move == "check":
        if player.wager != other.wager:
            raise Exception("You can't check. You haven't bet enough.")
        player.check()

    elif move == "call":
        if other.wager < player.wager:
            raise Exception("You can't call when you're ahead on betting!")
        if player.pot - money < 0:
            raise Exception("You don't have enough money. Sorry.")
        player.call(other.wager)

    else:
        print("Not a valid move - try again")
        get_input(player, other)

    return player.wager

def betting():
    """Players bet against each other"""
    game.player1.wager = get_input(game.player1, game.player2)
    game.player2.wager = get_input(game.player2, game.player1)
    if game.player1.wager == player2.wager:
        return True
    elif game.player1.folded or game.player2.folded:
        return False
    else:
        betting()

def newround():
    game.table.cards = []
    game.player1.hand.cards =[]
    game.player2.hand.cards =[]
    game.player1.folded = False
    game.player2.folded = False
    preflop()

def preflop():
    # deal
    deal(game.deck, game.player1.hand.cards, 2)
    deal(game.deck, game.player2.hand.cards, 2)
    # betting
    if betting():
    # advance to next round
        flop()
    else:
        showdown()

def flop():
    # deal
    deal(game.deck, game.community_cards, 3)
    # betting
    if betting():
        # advance to next round
        turn()
    else:
        showdown()

def turn():
    # deal
    deal(game.deck, game.community_cards, 1)
    # betting
    if betting():
        # advance to next round
        river()
    else:
        showdown()

def river():
    # deal
    deal(game.deck, game.community_cards, 1)
    # betting
    betting()
    showdown()

def showdown():
    """Finds Winner Gives Money"""
    # return winner
    if game.player1.folded:
        game.player2.funds += game.table_pot
    elif game.player2.folded:
        game.player1.funds += game.table_pot
    else:
        winner = compare_hands(game.player1.pocket, game.player2.pocket, game.community_cards)
        if winner == "Player1":
            game.player1.funds += game.table_pot
        elif winner = "Player2":
            game.player2.funds += game.table_pot
        else:
            game.player1.funds += game.table_pot/2
            game.player2.funds += game.table_pot/2
