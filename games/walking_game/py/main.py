import sys

# Terrains
class Grass:
	def getChar(self):
		return '.'

# Direction enum
class d:
	right=0
	up=1
	left=2
	down=3

# Character characters (haha)
# seriously, the ascii characters for each player
# (enough for 3 players)
chars = 0
def getChars():
	global chars
	if chars == 0:
		chars += 1
		return {d.right:")",d.up:"n",d.left:"(",d.down:"u"}
	elif chars == 1:
		chars += 1
		return {d.right:">",d.up:"^",d.left:"<",d.down:"v"}
	elif chars == 2:
		chars += 1
		return {d.right:"3",d.up:"M",d.left:"E",d.down:"W"}

# The main Model
class Model:
	def __init__(self,width,height):
		self.key = 0
		self.players = {}
		#self.addPlayer("dummy")
		self.board = Board(width,height)

	def addPlayer(self,name):
		tempKey = self.key
		self.players[self.key] = Player(name)
		self.key += 1
		return tempKey

	def getPlayer(self,playerKey):
		return self.players[playerKey]

	def move(self,playerKey,way,amount=1):
		player = self.players[playerKey]
		self.players[playerKey].move(way,amount)

	def face(self,playerKey,way):
		self.players[playerKey].face(way)

	def toString(self):
		outStr = ''
		for index in self.players:
			outStr += self.players[index].toString()
		outStr += self.board.toString(self.players)
		return outStr

# The Board of the Model
class Board:
	def __init__(self,width,height):
		self.width=width
		self.height=height
		self.terrain = []
		for i in range(0,height):
			self.terrain.append([])
			for j in range(0,width):
				self.terrain[i].append(Grass())

	def toString(self, players):
		outStr = '\nwidth: ' + str(self.width) + ' height: ' + str(self.height) + '\n'
		outArray = []
		for i in range(0,self.height):
			outArray.append([])
			for j in range(0,self.width):
				outArray[i].append(self.terrain[i][j].getChar())

		for player in players.values():
			outArray[player.loc.y][player.loc.x] = player.getChar()

		for i in range(self.height-1,-1,-1):
			for j in range(0,self.width):
				outStr += outArray[i][j]
			outStr += '\n'
		return outStr

# Individual Loc of a Board
class Loc:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.bear = d.right

	def move(self,way,amount):
		if way == d.right:
			self.x += amount
		elif way == d.up:
			self.y += amount
		elif way == d.left:
			self.x -= amount
		elif way == d.down:
			self.y -= amount
		self.bear = way

	def face(self,way):
		self.bear = way

	def toString(self):
		outStr = ''
		outStr += "X:    " + str(self.x) + ' '
		outStr += "Y:    " + str(self.y) + ' '
		outStr += "Dire: " + str(self.bear) + ' '
		return outStr

# Player in a Model
class Player:
	def __init__(self,name):
		self.name = name
		#self.char = name[0]
		self.health = 5
		self.mana = 5
		self.loc = Loc(0,0)
		self.chars = getChars()

	def move(self,way,amount=1):
		self.loc.move(way,amount)

	def face(self,way):
		self.loc.face(way)

	def getChar(self):
		return self.chars[self.loc.bear]
		#return self.char

	def toString(self):
		outStr = ''
		outStr += "Name:   " + str(self.name) + ' '
		outStr += "Health: " + str(self.health) + ' '
		outStr += "Mana:   " + str(self.mana) + ' '
		outStr += "Loc:    " + self.loc.toString()
		return outStr

# Handle keypresses
def handle(toParseFull):
	for toParse in toParseFull:
		if toParse == 'q':
			global going
			going = False
		k = 0
		if toParse == 'd':
			model.move(k,d.right)
		elif toParse == 'w':
			model.move(k,d.up)
		elif toParse == 'a':
			model.move(k,d.left)
		elif toParse == 's':
			model.move(k,d.down)
		elif toParse == 'D':
			model.face(k,d.right)
		elif toParse == 'W':
			model.face(k,d.up)
		elif toParse == 'A':
			model.face(k,d.left)
		elif toParse == 'S':
			model.face(k,d.down)
		k = 1
		if toParse == 'l':
			model.move(k,d.right)
		elif toParse == 'i':
			model.move(k,d.up)
		elif toParse == 'j':
			model.move(k,d.left)
		elif toParse == 'k':
			model.move(k,d.down)
		elif toParse == 'L':
			model.face(k,d.right)
		elif toParse == 'I':
			model.face(k,d.up)
		elif toParse == 'J':
			model.face(k,d.left)
		elif toParse == 'K':
			model.face(k,d.down)

# Main Function (go go go)
w = 30
h = 20
model = Model(w,h)
going = True
def main():
	model.addPlayer("Q")
	model.addPlayer("E")
	print model.toString()
	while going:
		handle(str(raw_input()))
		print model.toString()

main()
