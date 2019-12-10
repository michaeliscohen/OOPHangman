import pygame
from mob import Mob
from hanged import Hanged
from game_interaction import GameInteraction

# Class responsible for the Game Screen. Utilizes the mob, hanged, and game_interaction classes
class Gamepage(object):

	def __init__(self, mode, category):
		'''
	    Desc: initializes the game screen and its respective features
	    Args: self, mode, category
	    Return: N/A
	    '''
		self.bg = pygame.image.load('assets/images/background2.jpg')
		self.bg = pygame.transform.scale(self.bg, (1920, 1080))
		self.mob = Mob()
		self.hanged = Hanged()
		self.game = GameInteraction(mode, category)

	def click(self, win, mouse_pos):
		'''
	    Desc: Responds to click location and reacts accordingly
	    Args: self, win, mouse_pos
	    Return: response
	    '''
		response = self.game.click(win, mouse_pos)
		if(response == "wrong"):
			self.mob.negative()
		elif(response == "right"):
			self.mob.positive()
		if(response == "pass"):
			return self.hanged.click(mouse_pos)

		return response

	def draw(self, win):
		'''
	    Desc: Draws the on-screen features
	    Args: self, win
	    Return: N/A
	    '''
		win.blit(self.bg, (0, 0))
		self.mob.draw(win)
		self.hanged.draw(win)
		self.game.draw(win)