
class StandardGun:
	def __init__(self):
		self.level = 0
		def fire(target):
			target.health -= 1
		self.actions =  [fire]
	def act(self,actnum,target):
		self.actions[actnum](target)

class StardardRocket:
	def __init__(self):
		self.level = 1
		def blast(target):
			target.health -= 3
		self.actions = [blast]
	def act(self,actnum,target):
		self.actions[actnum](target)

class EmptyPlugin:
	def __init__(self):
		self.level = 0
	def act(self,actnum,target):
		pass
