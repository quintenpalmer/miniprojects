import sys

class qgame:
	def __init__(self,width,height):
		self.player1 = player("Q")
		self.board = board(width,height)

	def getPlayer(self,playerNum):
		if playerNum == 1:
			return self.player1

class player:
	def __init__(self,name):
		self.name = name
		self.health = 5
		self.mana = 5
		self.loc = loc(0,0)

	def move(self,way,amount=1):
		self.loc.move(way,amount)

	def face(self,way):
		self.loc.face(way)

	def toString(self):
		outStr = ''
		outStr += "Name:   " + str(self.name) + ' '
		outStr += "Health: " + str(self.health) + ' '
		outStr += "Mana:   " + str(self.mana) + ' '
		outStr += "Loc:    " + self.loc.toString()
		return outStr

class board:
	def __init__(self,width,height):
		self.width=width
		self.height=height

class dire:
	right=0
	up=1
	left=2
	down=3

class loc:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.dire = dire.right

	def move(self,way,amount):
		if way == dire.right:
			self.x += amount
		elif way == dire.up:
			self.y += amount
		elif way == dire.left:
			self.x -= amount
		elif way == dire.down:
			self.y -= amount
		self.dire = way

	def face(self,way):
		self.dire = way

	def toString(self):
		outStr = ''
		outStr += "X:    " + str(self.x) + ' '
		outStr += "Y:    " + str(self.y) + ' '
		outStr += "Dire: " + str(self.dire) + ' '
		return outStr

q = qgame(20,10)
going = True
width = 20
height = 10
reg = False

def handle(toParseFull):
	for toParse in toParseFull:
		if toParse == 'q':
			global going
			going = False
		elif toParse == 'd':
			q.getPlayer(1).move(dire.right)
		elif toParse == 'w':
			q.getPlayer(1).move(dire.up)
		elif toParse == 'a':
			q.getPlayer(1).move(dire.left)
		elif toParse == 's':
			q.getPlayer(1).move(dire.down)
		elif toParse == 'D':
			q.getPlayer(1).face(dire.right)
		elif toParse == 'W':
			q.getPlayer(1).face(dire.up)
		elif toParse == 'A':
			q.getPlayer(1).face(dire.left)
		elif toParse == 'S':
			q.getPlayer(1).face(dire.down)

def display(qg):
	x = q.getPlayer(1).loc.x
	y = q.getPlayer(1).loc.y
	face = q.getPlayer(1).loc.dire

	right = 0
	top = 0
	left = 0
	bottom = 0
	if face == dire.right:
		right = 1
	elif face == dire.up:
		top = 1
	elif face == dire.left:
		left = -1
	elif face == dire.down:
		bottom = -1

	global reg
	if reg:
		sys.stdout.write('\33['+str(height*2+2)+'A')
	else:
		reg = True
	sys.stdout.write(q.getPlayer(1).toString()+'\n')
	# all lines above user
	for i in range(y+1+top,height):
		for j in range(-width,width):
			sys.stdout.write('.')
		sys.stdout.write('\n')
	if top != 0:
		for j in range(-width,x):
			sys.stdout.write('.')
		sys.stdout.write('^')
		for j in range(x+1,width):
			sys.stdout.write('.')
		sys.stdout.write('\n')

	# all lines at user
	for i in range(-width,x+left):
		sys.stdout.write('.')
	if left != 0:
		sys.stdout.write('<')
	sys.stdout.write('x')
	if right != 0:
		sys.stdout.write('>')
	for i in range(x+1+right,width):
		sys.stdout.write('.')
	sys.stdout.write('\n')

	# all lines below user
	if bottom != 0:
		for j in range(-width,x):
			sys.stdout.write('.')
		sys.stdout.write('v')
		for j in range(x+1,width):
			sys.stdout.write('.')
		sys.stdout.write('\n')
	for i in range(-height,y+bottom):
		for j in range(-width,width):
			sys.stdout.write('.')
		sys.stdout.write('\n')

display(q)
while going:
	handle(str(raw_input()))
	display(q)
