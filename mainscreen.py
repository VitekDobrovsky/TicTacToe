import pygame 
from settings import *
from level import Level


class mainscreen:
	def __init__(self):
		self.screen = pygame.display.get_surface()

		self.multiplayer = Button((200, 60), 'multiplayer', 'fonts/LANDEPZ.ttf', (300, 350), RED, BLUE, self.multiplayergame)
		self.singleplayer = Button((200, 60), 'singleplayer', 'fonts/LANDEPZ.ttf', (300, 250), RED, BLUE, self.singleplayergame)

		self.run = False
		self.multigame = Level('multiplayer')
		self.singlegame = Level('singleplayer')

	def draw_text(self, text, path, size, pos, color):
		font = pygame.font.Font(path, size)
		text_surf = font.render(text, True, color)
		text_rect = text_surf.get_rect(center = pos)
		self.screen.blit(text_surf, text_rect)

	def multiplayergame(self):
		self.multigame.update()
		self.run = True

	def singleplayergame(self):
		self.singlegame.update()
		self.run = True

		

	def update(self):
		if not self.run:
			self.draw_text('Tac', 'fonts/INFECTED.ttf', 100, (300, 100), RED)
			self.draw_text('Tic', 'fonts/INFECTED.ttf', 100, (150, 100), BLUE)
			self.draw_text('Toe', 'fonts/INFECTED.ttf', 100, (450, 100), BLUE)
			self.multiplayer.draw()
			self.singleplayer.draw()
		self.multiplayer.check_click()
		self.singleplayer.check_click()



class Button:
	def __init__(self, size, text, path_to_font, pos, color, text_color, action):
		self.screen = pygame.display.get_surface()

		self.size = size
		self.text = text
		self.path_to_font = path_to_font
		self.pos = pos
		self.color = color
		self.text_color = text_color
		self.action = action

		self.clicked = False
		self.background = pygame.Surface(size)
		self.background.fill(color)
		self.bckgrnd_rect = self.background.get_rect(center = self.pos)
		self.can_click = True

	def check_click(self):
		mouse = pygame.mouse.get_pos()

		if not self.clicked:
			if self.bckgrnd_rect.collidepoint(mouse):
				if pygame.mouse.get_pressed()[0] and self.can_click:
					self.clicked = True	
					self.screen.fill('black')
					self.can_click = False

		if self.clicked:
			self.action()

	def draw(self):
		self.screen.blit(self.background, self.bckgrnd_rect)
		mainscreen().draw_text(self.text,self.path_to_font, 20, self.pos, self.text_color)

