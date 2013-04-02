import sys

colors = {
'red':'31',
'orange':'34',
'green':'32',
'turquoise':'36',
'blue':'33',
'violet':'35'}

def color_string(string,color,newline=False):
	return '\33['+colors[color]+'m'+str(string)+'\33[0m'

# NODES (for REVERSE AND CYCLE)
class emptyNode:
	def toStr(self):
		return color_string('emptyNode','green')+'()'
	def reverse(self,to):
		return to
	def empty(self):
		return True

class lnode:
	def __init__(self,val,size=0):
		if size > 0:
			self.val = size
			self.nex = lnode(val,size-1)
		else:
			self.val = val
			self.nex = emptyNode()

	def pointTo(self,nex):
		self.nex = nex

	def toStr(self):
		outStr = color_string('lnode','green')
		outStr += '('
		outStr += color_string(self.val,'red')
		outStr += ', '
		outStr += self.nex.toStr()
		outStr += ')'
		return outStr

	def reverse(self,to=emptyNode()):
		tmp = self.nex
		ret = self.nex.reverse(self)
		self.nex = to
		return ret

	def empty(self):
		return False

# REVERSE (of NODEs)
def llist(size):
	return lnode(0,size=size-1)

def llistIter(size):
	current = lnode(0)
	old = current
	for i in xrange(1,size):
		current = lnode(i)
		current.nex = old
		old = current
	return old


def create_cycle(size):
	first = current = lnode(0)
	old = current
	for i in range(1,size):
		current = lnode(i)
		current.nex = old
		old = current
	first.nex = old
	return old

# CYCLE (of NODEs)
def hasCycle(node):
	tort = node
	if not tort.empty():
		hare = tort.nex
	else:
		return False
	while hare != tort:
		if not hare.empty():
			hare = hare.nex
			if not hare.empty():
				hare = hare.nex
			else:
				return False
		else:
			return False
		tort = tort.nex
		if tort == hare:
			return True

if __name__ == "__main__":
	recursive_linked_list = llist(10)
	print recursive_linked_list.toStr()
	reversed_linked_list = recursive_linked_list.reverse()
	print reversed_linked_list.toStr()
	iterative_linked_list = llistIter(10)
	print iterative_linked_list.toStr()
	reversed_iterative_linked_list = iterative_linked_list.reverse()
	print reversed_iterative_linked_list.toStr()
	cyclic_linked_list = create_cycle(10)
	print "Should have and :", hasCycle(cyclic_linked_list)
	print "Shouldn't have and :", hasCycle(recursive_linked_list)
