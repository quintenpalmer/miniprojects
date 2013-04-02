from Plugin import EmptyPlugin

class Acceptor:
	def __init__(self,level):
		self.level = level
		self.plugin = EmptyPlugin
	def canAccept(self,plugin):
		if self.level >= plugin.level:
			return True
		else:
			return False
	def accept(self,plugin):
		if self.canAccept(plugin):
			self.plugin = plugin
			return True
		else:
			return False

levelMap = {
0 : (0),
0 : (0,0),
1 : (0,1),
2 : (0,0,1),
4 : (0,0,1,1),
5 : (0,0,1,2)
}

class AcceptorSet:
	def __init__(self,level):
		self.acceptors = []
		try:
			tmp = levelMap[level]
		except IndexError:
			print "invalid level given, default level 0 assigned"
			tmp = levelMap[0]
		for i in tmp:
			self.acceptors.append(Acceptor(i))
