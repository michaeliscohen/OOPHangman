import pygame

# Class responsible for displaying hanging man. Based on the errors, it adds parts to the man
class Hanged(object):

	def __init__(self):
		'''
	    Desc: Loads in and places the images respectively
	    Args: self
	    Return: N/A
	    '''
		self.post = pygame.image.load('assets/images/post.png')
		self.post = pygame.transform.scale(self.post, (436, 800))
		self.noose = pygame.image.load('assets/images/noose.png')
		self.head = pygame.image.load('assets/images/HEAD.png')
		self.head = pygame.transform.scale(self.head, (70, 70))
		self.arm_left = pygame.image.load('assets/images/ARM.png')

		self.arm_right = pygame.transform.flip(self.arm_left, False, True)
		self.leg_left = pygame.image.load('assets/images/LEG.png')

		self.leg_right = pygame.transform.flip(self.leg_left, False, True)
		
		self.torso = pygame.image.load('assets/images/TORSO.png')
		self.hand_left = pygame.image.load('assets/images/ez_hand.png')
		self.hand_right = pygame.transform.flip(self.hand_left, True, False)

		self.frown = pygame.image.load('assets/images/EZ_FROWN.png')
		self.frown = pygame.transform.scale(self.frown, (70, 70))
		self.menu = pygame.image.load('assets/images/MENU.png')
		self.retry = pygame.image.load('assets/images/RETRY.png')

		self.menu = pygame.transform.scale(self.menu, (150, 100))
		self.retry = pygame.transform.scale(self.retry, (150, 100))


		self.errors = 0

	def increase_error(self):
		'''
	    Desc: Accumulates the error count
	    Args: self
	    Return: N/A
	    '''
		self.errors += 1

	def click(self, mouse_pos):
		'''
	    Desc: Tracks coordinate of click and determines whether to go to the menu or to retry
	    Args: self, mouse_pos
	    Return: "menu" or "retry"
	    '''
		if(30 < mouse_pos[0] < 180 and 30 < mouse_pos[1] < 130 ):
			return "menu"
		elif(1750 < mouse_pos[0] < 1900 and 30 < mouse_pos[1] < 130 ):
			return "retry"
		return None

	def draw(self, win):
		'''
	    Desc: Places the hangman body parts dependent on the error accumulation, as well as other features on screen.
	    Args: self, win
	    Return: N/A
	    '''
		win.blit(self.post, (90, 160))
		win.blit(self.noose, (387, 231))
		
		if self.errors > 0:
			win.blit(self.head, (450, 360))
		if self.errors > 1:
			win.blit(self.torso, (387, 387))
		if self.errors > 2:
			win.blit(self.arm_left, (340, 387))
		if self.errors > 3:
			win.blit(self.arm_right, (433, 387))
		if self.errors > 4:
			win.blit(self.leg_left, (360, 527))
		if self.errors > 5:
			win.blit(self.leg_right, (413, 527))
		if self.errors > 6:
			win.blit(self.frown, (450, 360))
		if self.errors > 7:
			win.blit(self.hand_left, (285, 445))
		if self.errors > 8:
			win.blit(self.hand_right, (490, 443))

		win.blit(self.menu, (30, 30))
		win.blit(self.retry, (1750, 30))