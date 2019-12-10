import pygame
import random

'''
This class is responsible for the angry mob of onlookers. This includes their positive and negative comments.
'''
class Mob(object):

	def __init__(self):
		'''
	    Desc: initializes the Mob on screen, as well as their text
	    Args: self
	    Return: N/A
	    '''
		self.people = pygame.image.load('assets/images/mob.png')
		self.bubble = pygame.image.load('assets/images/bubble.png')

		self.bubble = pygame.transform.scale(self.bubble, (300, 300))

		with open("assets/data/insults.txt") as file:
			self.insults = file.read().splitlines()  

		with open("assets/data/compliments.txt") as file:
			self.compliments = file.read().splitlines()

		self.font = pygame.font.Font('assets/fonts/Steampuff.otf', 24)

		self.comment = ""

	def positive(self):
		'''
	    Desc: Randomly pulls text from the positive word text file
	    Args: self
	    Return: self.comment
	    '''
		self.comment = random.choice(self.compliments)

	def negative(self):
		'''
	    Desc: Randomly pulls text from the negative text file
	    Args: self
	    Return: self.comment
	    '''
		self.comment = random.choice(self.insults)

	def draw(self, win):
		'''
	    Desc: draws the static mob picture, static bubble, and dynamic text
	    Args: self, win
	    Return: N/A
	    '''
		win.blit(self.people, (900, 580))
		win.blit(self.bubble, (1150, 335))

		text = self.font.render(self.comment, True, (0, 0, 0))
		win.blit(text, (1190, 430))