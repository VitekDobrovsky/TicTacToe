import pygame
from settings import *
from sys import exit
from mainscreen import mainscreen


class TicTacToe:
    def __init__(self):
        # setup
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tic Tac Toe')
        self.clock = pygame.time.Clock()
        self.mainscreen = mainscreen()

    def run(self):
        while True:
            # exiting game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # update screen
            self.mainscreen.update()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    TicTacToe().run()