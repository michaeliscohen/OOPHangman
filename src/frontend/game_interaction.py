import pygame
import sys
sys.path.insert(1, '../backend')
from hangman import Hangman


# It is the main part of game which displays guessed letters and empty blocks for unguessed letters.
class GameInteraction(object):

	def __init__(self, mode, category):
		'''
	    Desc: initializes the images that are affected by the in game events
	    Args: self, mode, category
	    Return: N/A
	    '''
		self.letter = pygame.image.load('assets/images/letterRectangle.png')
		self.round = pygame.image.load('assets/images/RoundRectangle.png')
		self.hangman = Hangman(mode, category)

		self.word_boxes = []
		self.alphabet_boxes = []
		for i in range(len(self.hangman.curr_word)):
			self.word_boxes.append(pygame.transform.scale(self.letter, (70, 70)))

		for i in range(26):
			self.alphabet_boxes.append(pygame.transform.scale(self.round, (50, 50)))

		self.font = pygame.font.Font('assets/fonts/TEXAT BOLD PERSONAL USE___.otf', 32)

	def draw(self, win):
		'''
	    Desc: Draws the on-screen keyboard and word-blocks
	    Args: self, win
	    Return: N/A
	    '''
		start_point = 960 - 100*len(self.word_boxes)//2

		for i in range(len(self.word_boxes)):
			win.blit(self.word_boxes[i], (start_point + i*100 + 15, 40))

			if(self.hangman.predicted_word[i] == 1):
				self.word_boxes[i] = pygame.transform.scale(self.round, (70, 70))
				text = self.font.render(self.hangman.curr_word[i], True, (0, 0, 0))
				win.blit(text, (start_point + i*100 + 38, 55))


		start_point = 960 - 60*5
		for i in range(len(self.alphabet_boxes)):
			text = self.font.render(chr(i + ord('A')) , True, (0, 0, 0))
			if self.hangman.already_checked(chr(i + ord('a'))):
				continue
			if(i < 9):
				win.blit(self.alphabet_boxes[i], (start_point + i*60 + 15, 150))
				win.blit(text, (start_point + i*60 + 28, 155))

			elif(i < 18):
				win.blit(self.alphabet_boxes[i], (start_point + (i-9)*60 + 15, 215))
				win.blit(text, (start_point + (i-9)*60 + 28, 220))

			elif(i < 27):
				win.blit(self.alphabet_boxes[i], (start_point + (i-18)*60 + 15, 280))
				win.blit(text, (start_point + (i-18)*60 + 28, 285))

	def click(self, win, mouse_pos):
		'''
	    Desc: Tracks clicks to determine whether or not the user's interaction with the keyboard is correct
	    Args: self, win, mouse_pos
	    Return: "pass" or "status"
	    '''
		row = 0
		if(150 < mouse_pos[1] < 190):
			row = 0
		elif(215 < mouse_pos[1] < 245):
			row = 1
		elif(280 < mouse_pos[1] < 329):
			row = 2
		else:
			return "pass"
		start_point = 960 - 60 * 5
		col = -1

		for i in range(9):
			if(row == 2 and i == 8):
				return "pass"
			if(start_point < mouse_pos[0] < start_point + 60):
				col = i
				break	
			start_point += 60

		if col == -1:
			return "pass"

		index = row*9 + col
		letter = chr(index + ord('a'))

		response = self.hangman.insert_letter(letter)

		if(response < 0):
			return "pass"

		elif(response == 0):
			status = "failed"
		elif(response == 1):
			status = "passed"
		elif (response == 2):
			status = "wrong"
		else:
			status = "right"

		return status