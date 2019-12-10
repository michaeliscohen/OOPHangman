import pygame

# Class responsible for last page of game. Either pass or fail
class Lastpage(object):

	def __init__(self, bg):
		'''
	    Desc: initializes the last screens
	    Args: self, bg
	    Return: N/A
	    '''
		self.bg = pygame.image.load('assets/images/' + bg + '.jpg')
		self.bg = pygame.transform.scale(self.bg, (1920, 1080))
		self.menu = pygame.image.load('assets/images/MENU.png')
		self.retry = pygame.image.load('assets/images/RETRY.png')

	def click(self, mouse_pos):
		'''
	    Desc: Tracks click location in order to execute Retry or Menu
	    Args: self, mouse_pos
	    Return: "menu" or "retry"
	    '''
		if(650 < mouse_pos[0] < 860 and 700 < mouse_pos[1] < 850 ):
			return "menu"
		elif(1040 < mouse_pos[0] < 1190 and 700 < mouse_pos[1] < 850 ):
			return "retry"
		return None

	def draw(self, win):
		'''
	    Desc: Inserts button images onto the ending screen
	    Args: self, win
	    Return: N/A
	    '''
		win.blit(self.bg, (0, 0))
		win.blit(self.menu, (650, 700))
		win.blit(self.retry, (1040, 700))