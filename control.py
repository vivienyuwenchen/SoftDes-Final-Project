"""
Run game and accept inputs.
"""
from poker import *
import view
from model import *
from pygame.locals import *

# As globals variables, place these at the outermost indentation.
# As constants, capitalize them.
BLACK = (0, 0, 0)  # Define background color
SCREEN_WIDTH = 800  # Define game screen size
SCREEN_HEIGHT = 500  # Define game screen size

if __name__ == "__main__":
    # Game Interface Parameters
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)

    # 400 would usefully be a constant too
    raise_button = Button('raise.png', screen, 50, 400)
    check_button = Button('check.png', screen, 250, 400)
    call_button = Button('call.png', screen, 450, 400)
    fold_button = Button('fold.png', screen, 650, 400)

    buttons = [raise_button, check_button, call_button, fold_button]
    # since you're only using these variable names once, you could also write
    # directly:
    buttons = [
        Button('raise.png', screen, 50, 400),
        Button('check.png', screen, 250, 400),
        Button('call.png', screen, 450, 400),
        Button('fold.png', screen, 650, 400)
    ]
    # or:
    game = Game(False, True, screen)
    episode = []
    run_status = 'go'
    running = True
    while running:
        clock.tick(30)
        screen.fill(BLACK)
        view.update_display(screen, game, buttons)

        run_status = update_game(game, episode, buttons, run_status)
        pygame.display.update()
        player1_money = game.player1.funds
        player2_money = game.player2.funds
        # parens not needed
        if player1_money == 0:
            running = False
            print("GameOver Player 1 is out of money.")

        if player2_money == 0:
            running = False
            print("GameOver Player 2 is out of money.")

        # if you define player.__str__, you can write:
        for player in [game.player1, game.player2]:
            if player.funds == 0:
                running = false
                print("GameOver {} is out of money.".format(player))
        # This removes some copy-paste (less risk of a typo in one of the two
        # strings, or them getting out of sync in other ways as you edit the
        # code over time). It's also a step towards generalizing the game
        # to different number of players.
        #
        # Better: if Game has a property Game.players that it initializes
        # to [player1, player2], this loop can start:
        #   for player in Game.players:
        # This reads better, and is another step towards generalizing (and
        # not at the expense of readability, which is a nice two-fer).
