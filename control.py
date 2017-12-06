"""
Run game and accept inputs. Could split document here.
"""
# import viewer
from poker import *
from montecarlo import *
import view
from model import *
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
        view.update_display(screen,game,buttons)

        user_in = get_user_input(buttons)
        if user_in:
            print(user_in)

        #update_game(game, input)
        """update game is going to the main file of model, which will deal with
        storing the current state of the game, responding to user input,
        generating bot input, and updating the game
        """

        pygame.display.update()
