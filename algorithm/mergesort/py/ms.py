def ms(l):
	if len(l) > 2:
		lh,rh=mssplit(l)
		ret=[]
		for i in range(len(l)):
			if len(rh)==0 or (len(lh)>0 and rh[0] > lh[0]):
				ret.append(lh.pop(0))
			else:
				ret.append(rh.pop(0))
		return ret
	elif len(l)==2 and l[0] > l[1]:
		return [l[1],l[0]]
	else:
		return l
def mssplit(l):
	half = len(l)/2
	return ms(l[:half]),ms(l[half:])

if __name__ == "__main__":
	import time

	with open('../size.txt','r') as f:
		size = int(f.readline().strip())
	createStart = time.time()
	pre = range(size-1,-1,-1)
	exp = range(size)
	createEnd = time.time()

	start = time.time()
	post = ms(pre)
	end = time.time()

	print "prep",createEnd-createStart
	print "toSort",end-start
	print exp==post
	f = open('../lists-py.txt','w')
	for i in range(size):
		f.write(str(post[i])+'\n')
	f.close()
	assert(exp==post)
