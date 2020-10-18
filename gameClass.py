import os, sys
#import pygame
#pygame.init()

STARTPATH = "C:\Games"

class GameClass:
	"This stores all of the game's data"
	def __init__(self):
		#Holds the name of the game.  MUST be stored in "Title.txt"
		self.title = None
		#Holds the path to the game's executable
		self.game = None
		#Holds the path to the image file to be displayed in the arcade
		#	Image MUST be 480 x 480 pixels
		self.image = None
		#Holds the path to the text file with info about the game.
		#	MUST be called "Info.txt"
		self.info = None
		#Holds the path to the text file with game's controls.
		#	MUST be called "Controls.txt"
		self.controls = None
		#Holds the path to a music file to be played when people scroll
		#	over the game in the arcade.  MUST be an .mp3
		self.music = None
		#Holds the number of thumbs up people have given the game.
		self.ratings = 0

	def SetTitle(self, titlePath):
		file = open(titlePath, 'r')
		self.title = file.read()
		file.close()

	def SetGame(self, filePath):
		self.game = filePath

	def SetImage(self, imagePath):
		self.image = imagePath

	def SetInfo(self, infoPath):
		self.info = infoPath

	def SetControls(self, ctrlPath):
		self.controls = ctrlPath

	def SetMusic(self, musicPath):
		self.music = musicPath

	def AddRating(self, score):
		self.ratings = self.ratings + 1

	def Title(self):
		return self.title

	def Rating(self):
		return self.ratings

class GameListClass:
	"Generates and stores a list of all the games in the system"

	def __init__(self):
		self.gamesList = self.GenerateGameList()


	def GenerateGameList(self):
		folders = os.listdir(STARTPATH)
		list = []
		game = GameClass()
		add = False
		alreadyAdded = False

		#Finds all of the relevant information for each game
		for folder in folders:
			temp = os.path.join(STARTPATH, folder)
			temp2 = os.listdir(temp)

			for file in temp2:
				path = os.path.join(temp, file)
				path = '%s' %(path)

				if file == "Title.txt":
					game.SetTitle(path)
					add = True
				if file.endswith(".exe"):
					game.SetGame(path)
					add = True
				if file.endswith(".jpg"):
					game.SetImage(path)
					add = True
				if file == "Info.txt":
					game.SetInfo(path)
					add = True
				if file == "Controls.txt":
					game.SetControls(path)
					add = True
				if file.endswith(".mp3"):
					game.SetMusic(path)
					add = True

			for g in self.gamesList:
				if game.Title == g.Title:
					alreadyAdded = True
					break

			if not alreadyAdded and add:
				list.append(game)
				game = GameClass()
				add = False

			alreadyAdded = False

		return list

	def UpdateList(self):
		self.gamesList = self.GenerateGameList()

	def _PrintGames(self):
		for game in self.gamesList:
			print("Game's title is: %s" %game.title)
			print("Game's game path is: %s" %game.game)
			print("Game's image path is: %s" %game.image)
			print("Game's info path is: %s" %game.info)
			print("Game's control path is: %s" %game.controls)
			print("Game's music path is: %s" %game.music)
			print("Game's rating is: %s" %game.ratings)
