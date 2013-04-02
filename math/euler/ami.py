#!/usr/bin/env python
from pprint import pprint
import math
import sys
import time

def even_div(num,div):
	return float(num)/div == num/div

def find_even_div(num):
	even_divs = []
	for div in range(1,int(math.sqrt(num))+1):
		if even_div(num,div):
			even_divs.append(div)
			even_divs.append(num/div)
	even_divs = remove_dup(even_divs)
	even_divs.remove(num)
	return even_divs

def remove_dup(l):
	ret = []
	for i in l:
		if not i in ret:
			ret.append(i)
	return ret

def find_sum(l):
	s = 0
	for i in l:
		s += i
	return s

def find_amis(total):
	sums = [0]
	amis = []
	for i in range(1,total+1):
		s = find_sum(find_even_div(i))
		sums.append(s)
	for i in range(1,total+1):
		try:
			if sums[sums[i]] == i and i != sums[i]:
				amis.append(i)
		except IndexError:
			pass
	return find_sum(amis)

if len(sys.argv) == 2:
	start = time.time()
	print find_amis(int(sys.argv[1]))
	print 'time:'+str(time.time()-start)
