import pygame
import time
from settings import *


class Level:
    def __init__(self, game_type):
        # setup
        self.screen = pygame.display.get_surface()
        self.tiles = [TILE1_rect, TILE5_rect, TILE3_rect, TILE7_rect,
                     TILE6_rect, TILE8_rect, TILE4_rect, TILE9_rect, TILE2_rect]
        self.game_type = game_type

        # click setup
        self.can_click = True
        self.click_index = 0
        self.clicked_time = None

        # win setup
        self.tie = False

        # black screen at start
        self.can_black = False

    def draw_grid_vertical(self):
        x = 0
        y = 0
        width = 1
        for i in range(4):
            if x == 0:
                width = 5
                x = 2
            elif x == 202:
                width = 1
                x = 200
            elif x == 600:
                width = 5
                x = 597
            else:
                width = 1

            pygame.draw.line(self.screen, LINE_COLOR, (x,y),(x,HEIGHT), width)

            x += 200

    def draw_grid_horizontal(self):
        x = 0
        y = 0
        width = 1
        for i in range(4):
            if y == 0:
                width = 5
                y = 2
            elif y == 202:
                width = 1
                y =  200
            elif y == 600:
                width = 5
                y = 597
            else:
                width = 1

            pygame.draw.line(self.screen, LINE_COLOR, (x,y),(WIDTH,y), width)

            y += 200

    def draw_on_click(self):
        mouse = pygame.mouse.get_pos()
        for tile in self.tiles:
            # multiplayer game
            x = round(tile.topleft[0] / 100)
            y = round(tile.topleft[1] / 100)
            if tile.collidepoint(mouse):
                if pygame.mouse.get_pressed()[0] and self.can_click:

                    self.clicked_time = pygame.time.get_ticks()

                    if BOARD[x][y] == 0:
                        if self.click_index == 1 or self.click_index == 3 or self.click_index == 5 or self.click_index == 7 or self.click_index == 9:
                            circle = Circle(tile.centerx, tile.centery)
                            circle.draw()
                            BOARD[x][y] = 1
                        elif self.click_index == 2 or self.click_index == 4 or self.click_index == 6 or self.click_index == 8:
                            if self.game_type == 'multiplayer':
                                cross = Cross(tile.centerx, tile.centery)
                                cross.draw()
                                BOARD[x][y] = 2

                        self.click_index += 1
                        self.can_click = False
            # bot
            if self.game_type == 'singleplayer' and self.can_click:
                if self.click_index == 2 or self.click_index == 4 or self.click_index == 6 or self.click_index == 8:
                    if BOARD[x][y] == 0:
                        self.clicked_time = pygame.time.get_ticks()
                        cross = Cross(tile.centerx, tile.centery)
                        cross.draw()
                        BOARD[x][y] = 2

                        self.click_index += 1
                        self.can_click = False


    def isWinner(self, bo, index):
        return (bo[0][0] == index and bo[0][2] == index and bo[0][4] == index) or (bo[2][0] == index and
        bo[2][2] == index and bo[2][4] == index) or (bo[4][0] == index and
        bo[4][2] == index and bo[4][4] == index) or (bo[0][0] == index and
        bo[2][0] == index and bo[4][0] == index) or (bo[0][2] == index and
        bo[2][2] == index and bo[4][2] == index) or (bo[0][4] == index and
        bo[2][4] == index and bo[4][4] == index) or (bo[0][0] == index and
        bo[2][2] == index and bo[4][4] == index) or (bo[0][4] == index and
        bo[2][2] == index and bo[4][0] == index)

    def check_win(self):
        if self.isWinner(BOARD, 1):
            self.win_screen('circle', False)
            self.tie = True
        elif self.isWinner(BOARD, 2):
            self.win_screen('cross', False)
            self.tie = True
        elif self.click_index == 10:
            self.win_screen('cross', True)
            self.tie = True
        else:
            self.tie = False

    def win_screen(self, index, tie):
        # fade away
        back_fade = pygame.Surface((600,600))
        back_fade.fill('black')
        back_fade_rect = back_fade.get_rect(topleft = (0,0))
        time.sleep(0.02)
        back_fade.set_alpha(10)
        self.screen.blit(back_fade, back_fade_rect)

        # image of winner
        path = f'images/{index}.png'
        winner = pygame.image.load(path).convert_alpha()
        winner_rect = winner.get_rect(center = (300, 300))
        winner.set_alpha(90)
        if not tie:
            self.screen.blit(winner, winner_rect)
        
        # if tie
        circle = pygame.image.load('images/circle.png')
        cross = pygame.image.load('images/cross.png')
        circleRect = circle.get_rect(center = (300 + 85.3, 300))
        crossRect = cross.get_rect(center = (300 - 85.3, 300))
        cross.set_alpha(100)
        circle.set_alpha(100)
        if tie:
            self.screen.blit(cross, crossRect)
            self.screen.blit(circle, circleRect)

        # text
        if index == 'circle':
            color = RED
        elif index == 'cross':
            color = BLUE 
        font = pygame.font.Font('fonts/LANDEPZ.ttf', 70)
        text = f'{index} win' if not tie else 'tie'
        winText = font.render(text, True, color)
        winRect = winText.get_rect(midtop = (winner_rect.midbottom[0], winner_rect.midbottom[1] - 20))
        self.screen.blit(winText, winRect)

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if not self.can_click:
            if current_time - self.clicked_time >= 300:
                self.can_click = True
    
    def update(self):
        # draw grid
        if not self.tie:
            self.draw_grid_vertical()
            self.draw_grid_horizontal()

        # making circles and crosses
        self.draw_on_click()
        self.cooldown()

        # win part
        self.check_win()


class Circle:
    def __init__(self, x, y):
        self.screen = pygame.display.get_surface()
        self.image = pygame.image.load('images/circle.png').convert_alpha()
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (170, 170))
        self.rect = self.image.get_rect(center = (x,y))


    def draw(self):
        self.screen.blit(self.image, self.rect)

class Cross:
    def __init__(self, x, y):
        self.screen = pygame.display.get_surface()
        self.image = pygame.image.load('images/cross.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (170, 170))
        self.rect = self.image.get_rect(center = (x,y))

    def draw(self):
        self.screen.blit(self.image, self.rect)
