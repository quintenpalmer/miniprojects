#!/usr/bin/env python

def fib(nth):
	curr = 1
	old = 0
	for i in range(nth):
		tmp = curr
		curr = curr+old
		old = tmp
	return curr;

if __name__ == "__main__":
	import sys
	nth = 13
	if len(sys.argv) == 2:
		nth = int(sys.argv[1])
	print "fib of %s is %ls"%(nth,fib(nth))
