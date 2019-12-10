import pygame
from frontpage import Frontpage
from gamepage import Gamepage 
from game_over import Lastpage
import json

# Main frontend class which connects all the game modules. The pygame display is initialized and managed.
class Controller(object):

	def __init__(self):
		'''
		Desc: Initializes pygame and its display/sound 
		Args: self
		Return: N/A
		'''
		pygame.init()

		pygame.mixer.init()
		pygame.mixer.music.load('assets/music/ambient.wav')
		pygame.mixer.music.play(-1)

		self.boo_sound = pygame.mixer.Sound('assets/music/boo.wav')
		self.cheer_sound = pygame.mixer.Sound('assets/music/cheer.wav')


		pygame.font.init()
		self.win = pygame.display.set_mode((1920, 1080))
		pygame.display.set_caption("Hangman by the Pawn Stars")
		self.run = True
		self.start_page = Frontpage()
		
		self.game_mode = 0
		self.clock = pygame.time.Clock()
		self.run_game()

	# Management of events on the main menu screen
	def event_front_page(self):
		'''
		Desc: Accounts for events that may occur on the menu screen 
		Args: self
		Return: N/A
		'''
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.run = False
			if(event.type == pygame.MOUSEBUTTONDOWN):
				mouse_pos = event.pos
				response = self.start_page.click(mouse_pos)
				if(response != None):
					self.start_game(response)
		
	# This method is responsible for adding to the JSON file for data permanence
	def update_json(self, win):
		'''
		Desc: Writes player data to a JSON file for data permanence
		Args: self, win
		Return: N/A
		'''
		data = {"streak" : 0, "wins" : 0, "played" : 0, "win_percent" : 0}

		try:
			with open("data_file.json", "r") as read_file:
				data = json.load(read_file)
		except:
			pass
		if win == 1:
			data["streak"] += 1
			data["wins"] += 1

		else:
			data["streak"] = 0

		data["played"] += 1
		data["win_percent"] = round(100*data["wins"]/data["played"])

		with open("data_file.json", "w") as write_file:
			json.dump(data, write_file)


	#Loss screen from Return Key 2
	def failed_game(self):
		'''
		Desc: Sends screen to game over(loss) from Return Key 2
		Args: self
		Return: N/A
		'''
		self.game_mode = 2
		self.last_page = Lastpage("game_over_screen")
		self.update_json(0)

	#Win screen from Return Key 3
	def passed_game(self):
		'''
		Desc: Sends screen to victory screen from Return Key 3
		Args: self
		Return: N/A
		'''
		self.update_json(1)
		self.game_mode = 3
		self.last_page = Lastpage("win_screen")

	# This method adds responses to clicking the mouse
	def check_game_response(self, response):
		'''
		Desc: This method takes in the game response and reacts accordingly
		Args: self, response
		Return: N/A
		'''
		# print(response)
		if(response == "failed"):
			pygame.mixer.Sound.play(self.boo_sound)
			self.failed_game()
		elif (response == "passed"):
			pygame.mixer.Sound.play(self.cheer_sound)
			self.passed_game()
		elif (response == "wrong"):
			pygame.mixer.Sound.play(self.boo_sound)
			self.game_page.hanged.increase_error()
		elif (response == "right"):
			pygame.mixer.Sound.play(self.cheer_sound)
		elif (response == "retry"):
			self.start_game(self.old_reponse)
		elif (response == "menu"):
			self.game_mode = 0

	# A method to manage events when game is in progress
	def event_game_page(self):
		'''
		Desc: Accounts for events that may occur on game screen
		Args: self
		Return: N/A
		'''
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.run = False
			if(event.type == pygame.MOUSEBUTTONDOWN):
				mouse_pos = event.pos
				response = self.game_page.click(self.win, mouse_pos)
				self.check_game_response(response)

	# A method to manage events when on the end screen
	def event_last_page(self):
		'''
		Desc: Accounts for events that may occur on the ending screen
		Args: self
		Return: N/A
		'''
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.run = False
			if(event.type == pygame.MOUSEBUTTONDOWN):
				mouse_pos = event.pos
				response = self.last_page.click(mouse_pos)
				self.check_game_response(response)

	# This is the indefinite loop for determining the state of the game
	def run_game(self):
		'''
		Desc: The indefinite loop for determining the state of the game 
		Args: self
		Return: N/A
		'''
		while self.run:
			self.clock.tick(30)
			if self.game_mode == 0 :
				self.event_front_page()
			elif self.game_mode == 1:
				self.event_game_page()
			else:
				self.event_last_page()
			self.redraw_game_window()

		pygame.quit()

	# This method is called by clicking the start button on the menu screen
	def start_game(self, response):
		'''
		Desc: Sends the game onto the game screen
		Args: self, response
		Return: N/A
		'''
		self.old_reponse = response
		self.game_mode = 1
		self.game_status = "running"
		self.game_page = Gamepage(response["mode"], response["category"])

	# This method is responsible for the updating of the game screen
	def redraw_game_window(self):
		'''
		Desc: Updates the game window based on its current state
		Args: self
		Return: N/A
		'''
		if(self.game_mode == 0):
			self.start_page.draw(self.win)
		elif(self.game_mode == 1):
			self.game_page.draw(self.win)
		else:
			self.last_page.draw(self.win)
		pygame.display.update()