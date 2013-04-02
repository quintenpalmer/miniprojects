from Ship import Ship
from Plugin import *

class Model:
	def __init__(self):
		self.ship = Ship(1)
		self.ship.addPlugin(0,StandardGun())
		self.enemy = Ship()
		self.enemy.addPlugin(0,StandardGun())
