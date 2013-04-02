from random import randint

def randList(size):
	orig = range(size)
	ret = []
	for i in range(size-1,-1,-1):
		r = randint(0,i)
		ret.append(orig[r])
		del orig[r]
		'''
		print "r is : "+str(r)
		print "ret is now : "+str(ret)
		print "orig is now : "+str(orig)
		raw_input("hit me")
		'''
	return ret

if __name__ == "__main__":
	with open('../size.txt','r') as f:
		size = int(f.readline().strip())
	r = randList(size)
	print r
