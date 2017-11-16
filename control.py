"""
Run game and accept inputs. Could split document here.
"""
# import viewer

game = Game()
# initialize viewer
# viwer takes as input game and displays table

def get_input(player):
    """
    Get user or bot input.
    """
    # TODO: impliment this
    # if player.is_bot :
    # else:
    pass
def betting():
    """Players bet against each other"""
    # TODO: implement this
    # playerA bets
    # playerB bets
    # if playerA.wager = playerB.wager : return not folded
    # elif playerA.folded or playerB.folded : return folded
    # else repeat
    pass
def newround():
    game.table.cards = []
    game.player1.hand.cards =[]
    game.player2.hand.cards =[]
    game.player1.folded = False
    game.player2.folded = False
def preflop():
    # TODO: implement this
    # deal
    deal(game.deck, game.player1.hand.cards, 2)
    deal(game.deck, game.player2.hand.cards, 2)
    # bettting
    # advance to next round
    pass
def flop():
    # TODO: implement this
    # deal
    deal(game.deck, game.table.cards, 3)
    # bettting
    # advance to next round
    pass
def turn():
    # TODO: implement this
    # deal
    deal(game.deck, game.table.cards, 1)
    # bettting
    # advance to next round
    pass
def river():
    # TODO: implement this
    # deal
    deal(game.deck, game.table.cards, 1)
    # bettting
    # advance to next round
    pass
def showdown():
    """Finds Winner Gives Money"""
    # TODO: implement this
    # return winner
    pass
