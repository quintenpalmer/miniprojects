physical = 0
supernatural = 1
nature = 2
tech = 3
dark = 4
light = 5
class Attack:
	def __init__(self,amount,element,physical):
		self.amount = amount
		self.element = element
		self.physical = physical
class DummyAttack:
	def __init(self):
		self.amount = 0
		self.amount = physical
		self.physical = False
class Being:
	def giveAttack(self,num):
		try:
			return self.attacks[num]
		except IndexError:
			return DummyAttack()
	def receiveAttack(self,attack):
		element = attack.element
		amount = attack.amount
		if element in self.resists:
			self.health = self.health - int(amount/2)
		elif element in self.weaknesses:
			self.health = self.health - int(amount*2)
		elif element in self.immunes:
			pass
		elif element in self.absorbs:
			self.health = self.health + amount
		else:
			self.health = self.health - amount
	def toString(self):
		return self.name +' '+ str(self.health)
class Orc(Being):
	def __init__(self, color, name, age):
		self.color = color
		self.health = 30
		self.name = name
		self.age = age
		self.basepower = 4
		self.attacks = []
		self.attacks.append(Attack(2,nature,True))
		self.attacks.append(Attack(4,physical,True))
		self.element = nature
		self.physical = True
		self.resists = [nature,physical]
		self.weaknesses = [tech]
		self.immunes = [supernatural]
		self.absorbs = []

class Human(Being):
	def __init__(self,color,name,age):
		self.color = color
		self.health = 25
		self.name = name
		self.age = age
		self.basepower = 3
		self.attacks = []
		self.attacks.append(Attack(3,physical,True))
		self.attacks.append(Attack(2,tech,True))
		self.element = physical
		self.physical = True
		self.resists = []
		self.weaknesses = [supernatural,tech]
		self.immunes = []
		self.absorbs = [light]

class Ghost(Being):
	def __init__(self,color,name,age):
		self.color = color
		self.health = 15
		self.name = name
		self.age = age
		self.basepower = 2
		self.element = supernatural
		self.attacks = []
		self.attacks.append(Attack(3,supernatural,False))
		self.attacks.append(Attack(1,nature,False))
		self.physical = False
		self.resists = []
		self.weaknesses = [light]
		self.immunes = [physical,tech]
		self.absorbs = [dark]

class Being(Being):
	pass
f = open('races.txt','r')
fullfile = ''
for line in f:
	fullfile+=line
fileraces = fullfile.split(';')[:-1]
races = []
for filerace in fileraces:
	race = Being()
	fields = filerace.split(':')[1]
	race.health = int(fields.split('\n')[1].split('=')[1])
	race.basepower = int(fields.split('\n')[2].split('=')[1])
	races.append(race)

ocran = Orc('green','Ocran',13)
midas = Human('pale','Midas',50)
print ocran.toString(),',',midas.toString()
midas.receiveAttack(ocran.giveAttack(1))
print ocran.toString(),',',midas.toString()
