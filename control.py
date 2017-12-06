"""
Run game and accept inputs. Could split document here.
"""
# import viewer
from poker import *
from montecarlo import *
import view
import pygame,sys,inspect,random
from pygame.locals import *

def get_game_status(game):
    return [game.player1.pocket.cards, game.player2.pocket.cards, game.community_cards, game.player1.funds, game.player2.funds, game.table_pot]

def check_turn(game):
    if player.isturn:
        act = get_input(game.player1, buttons)
        if act:
            game.player1.move = act
            game.player1.isturn = False
            game.player2.isturn = True
            return act
    elif other.isturn:
        act = get_input(game.player2, buttons)
        if act:
            game.player2.move = act
            game.player1.isturn = True
            game.player2.isturn = False
            return act

def process_input(game, player, other):
    """
    Get user or bot input.
    """

    money = 100
    view.update_display(screen,game)

    move = check_turn(game)

    if move == "fold":
        player.fold()

    elif move == "raise": #player bets and abount
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

    else:
        print("Not a valid move - try again")
        process_input(game, player, other)

    return player.wager

def betting():
    """Players bet against each other"""
    game.player1.wager = process_input(game, game.player1, game.player2)
    print("Player 1:", game.player1.wager)
    print("Player 2:", game.player2.wager)

    game.update_tablepot()

    if game.player1.folded:
        print("player1 folded")
        return False

    game.player2.wager = process_input(game, game.player2, game.player1)
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

def newround(game):
    game.community_cards = []
    # deal
    game.player1.pocket = []
    game.player2.pocket = []
    deal(game.deck, game.player1.pocket, 2)
    deal(game.deck, game.player2.pocket, 2)
    game.player1.folded = False
    game.player2.folded = False

def preflop(game):
    print(game.player1.blind_type)
    print("Player 1:", game.player1.pocket)
    print("Player 2:", game.player2.pocket)

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

def get_input(player,buttons):
    if player.is_bot:
        """gets move from bot and updates trainer"""
        act = mc_control_epsilon_greedy(episode, game, player)
        return act
    else:
        for event in pygame.event.get():                                        # Check for events
            if event.type == QUIT:                                              # Allow the user to end the game at any time
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if raise_button.rect.collidepoint(event.pos):
                    act = "raise"
                    actions.append(act)
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

if __name__ == "__main__":
    # Game Interface Parameters
    black = (0, 0, 0)                       #  Define background color
    screen_width = 800                      #  Define game screen size
    screen_height = 500                     #  Define game screen size

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    #display_blank(screen)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)

    raise_button = Button('raise.png', screen, 50, 400)
    check_button = Button('check.png', screen, 250, 400)
    call_button = Button('call.png', screen, 450, 400)
    fold_button = Button('fold.png', screen, 650, 400)

    buttons = [raise_button, check_button, call_button, fold_button]

    game = Game(False, True, screen)

    episode = []
    while True:
        clock.tick(30)
        screen.fill(black)

        mouse_state = pygame.mouse.get_pressed()
        x,y = pygame.mouse.get_pos()

        for event in pygame.event.get():                                        # Check for events
            if event.type == QUIT:                                              # Allow the user to end the game at any time
                pygame.quit()
                sys.exit()
                
        #button = pygame.Rect(200, 100, 100, 50)
        #pygame.draw.rect(screen, (0,255,0), button)

        view.update_display(screen,game,buttons)

        pygame.display.update()
