import pygame, sys, inspect, random
from pygame.locals import *

actions = []
white = (255,255,255)

class Button(pygame.sprite.Sprite):
    """ Rudimentary card class to track suit and value """
    def __init__(self, picture, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image =  pygame.image.load(picture).convert_alpha()
        self.image.set_colorkey(white)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.centerx = self.x + (self.image.get_width()/2)
        self.rect.centery = self.y + (self.image.get_height()/2)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

def click_input(buttons):
    raise_button = buttons[0]
    check_button = buttons[1]
    call_button = buttons[2]
    fold_button = buttons[3]

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

    while True:
        clock.tick(30)
        screen.fill(black)

        mouse_state = pygame.mouse.get_pressed()
        x,y = pygame.mouse.get_pos()
        #button = pygame.Rect(200, 100, 100, 50)
        #pygame.draw.rect(screen, (0,255,0), button)
        raise_button.draw()
        check_button.draw()
        call_button.draw()
        fold_button.draw()

        user_in = click_input(buttons)
        if user_in:
            print(user_in)

        pygame.display.update()
