from Acceptors import *
from Status import Status

class Ship:
	def __init__(self,level=0):
		self.level = level
		self.health = (level+1)*5
		self.status = Status.normal
		self.acceptors = AcceptorSet(self.level)
	def addPlugin(self,acceptorIndex,plugin):
		return self.acceptors.acceptors[acceptorIndex].accept(plugin)
	def attack(self,weaponIndex,target):
		self.acceptors.acceptors[weaponIndex].plugin.act(0,target)
