import pygame

# settings
HEIGHT = 600
WIDTH = 600
TILE_SIZE = 200
FPS = 60
BOARD = [
	[0,'',0,'',0],
	[],
	[0,'',0,'',0],
	[],
	[0,'',0,'',0],
]


# colors 
LINE_COLOR = 'white'
RED = '#d90d17'
BLUE = '#0f97d1'
PURPLE = '#d900ff'


# Tiles
TILE_1 = pygame.Surface((200, 200))
TILE_2 = pygame.Surface((200, 200))
TILE_3 = pygame.Surface((200, 200))
TILE_4 = pygame.Surface((200, 200))
TILE_5 = pygame.Surface((200, 200))
TILE_6 = pygame.Surface((200, 200))
TILE_7 = pygame.Surface((200, 200))
TILE_8 = pygame.Surface((200, 200))
TILE_9 = pygame.Surface((200, 200))

TILE1_rect = TILE_1.get_rect(topleft = (0, 0))
TILE2_rect = TILE_2.get_rect(topleft = (200, 0))
TILE3_rect = TILE_3.get_rect(topleft = (400, 0))
TILE4_rect = TILE_4.get_rect(topleft = (0, 200))
TILE5_rect = TILE_5.get_rect(topleft = (200, 200))
TILE6_rect = TILE_6.get_rect(topleft = (400, 200))
TILE7_rect = TILE_7.get_rect(topleft = (0, 400))
TILE8_rect = TILE_8.get_rect(topleft = (200, 400))
TILE9_rect = TILE_9.get_rect(topleft = (400, 400))


