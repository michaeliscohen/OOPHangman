import random


# This class is responsible for the game logic, making it the backbone of the backend code.
class Hangman:

	def __init__(self, mode, category):
		'''
		Desc: Initializes the Hangman difficulties and words
		Args: self, mode (difficulty), category (filename of txt file)
		Return: N/A
		'''
		filename = "assets/data/" + category + ".txt"
		self.words = self.read_file(filename)
		if mode == "easy":
			self.max_attempts = 9
		else:
			self.max_attempts = 6

		self.reset()

	@staticmethod #Use of a static decorator due to the fact that an instance variable is not being used. If static method is not used, then positional argument error occurs.
	def read_file(filename):	
		'''
		Desc: Reads in the file containing the words
		Args: filename
		Return: A list of the categorical words to be selected
		'''
		with open (filename, 'r') as file:
			return file.read().splitlines()

	# Return Key: [-2]LETTER ALREADY GUESSED, [-1] INVALID INPUT, [0] DEFEAT, [1] VICTORY, [2] LETTER INCORRECT, [3] LETTER CORRECT
	def insert_letter(self, c):
		'''
		Desc: Allows the user to input a letter. The class will determine whether the letter chosen is correct or not, then accumulates successful and unsuccessful attempts
	    Args: self, c
	    Return: -2, -1, 0, 1, 2, or 3 depending on the scenario
		'''
		if(len(c) != 1):
			return -1 #One letter at a time
		if(ord(c) < ord('a') or ord(c) > ord('z')):
			return -1 #Character must be alphabetic

		if c in self.correct_letters:
			return -2 #Letter verified as correct
		if c in self.incorrect_letters:
			return -2 #Letter is incorrect

		flag = 0
		for i in range(self.word_size):
			if self.curr_word[i] == c:
				self.predicted_word[i] = 1
				self.predicted_word_count += 1
				flag = 1

		if(flag == 0): #if previous for loop is not successful
			self.num_attempts += 1
			self.incorrect_letters.add(c) 

			if (self.num_attempts == self.max_attempts):
				return 0 #Body parts are visual representation of num_attemps and max_attempts -- loss if max reached
			return 2 #this will execute until max attemps reached
		else:
			self.correct_letters.add(c)
			if self.check_win():
				return 1 #Victory is reached
			return 3 #This will execute until victory is reached

	# If the number of correct letters is equal to the length of the word, the game will end
	def check_win(self):
		'''
		Desc: Checks to see if the correct letters is equal to the length of the word
		Args: self
		return: equivalence between the two leads to victory
		'''
		return self.predicted_word_count == self.word_size

	# Verifies if a character is a duplicate
	def already_checked(self, c):
		'''
		Desc: Checks to see whether a letter is a duplicate
		Args: self, c
		return: character in the collection of correct letters or incorrect letters, c.
		'''
		return c in self.correct_letters or c in self.incorrect_letters

	def reset(self):
		'''
		Desc: Begins a new game. Executes within the __init__.
		args: self
		return: N/A
		'''
		self.curr_word = random.choice(self.words).lower()
		#print(self.curr_word) -- used for testing purposes
		self.word_size = len(self.curr_word)
		self.predicted_word = [0]*self.word_size
		self.correct_letters = set()
		self.incorrect_letters = set()
		self.predicted_word_count = 0
		self.num_attempts = 0