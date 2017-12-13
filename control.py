"""
Run game and accept inputs.
"""
from poker import *
import view
from model import *
from pygame.locals import *

if __name__ == "__main__":
    # Game Interface Parameters
    black = (0, 0, 0)                       #  Define background color
    screen_width = 800                      #  Define game screen size
    screen_height = 500                     #  Define game screen size

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)

    raise_button = Button('raise.png', screen, 50, 400)
    check_button = Button('check.png', screen, 250, 400)
    call_button = Button('call.png', screen, 450, 400)
    fold_button = Button('fold.png', screen, 650, 400)

    buttons = [raise_button, check_button, call_button, fold_button]
    game = Game(False, True, screen)
    episode = []
    run_status = 'go'
    running = True
    while running:
        clock.tick(30)
        screen.fill(black)
        view.update_display(screen,game,buttons)

        run_status = update_game(game, episode, buttons,run_status)
        pygame.display.update()
        player1_money = game.player1.funds
        player2_money = game.player2.funds
        if (player1_money == 0):
            running = False
            print("GameOver Player 1 is out of money.")

        if (player2_money ==0 ):
            running = False
            print("GameOver Player 2 is out of money.")
           