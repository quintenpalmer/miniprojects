#!/usr/bin/env python
import sys

def thue_morse(length):
	base = [0]
	for i in range(length):
		for index in range(len(base)):
			base.append(int(not base[index]))
	return base

def print_thue_morse(length):
	for val in thue_morse(length):
		sys.stdout.write(str(val))
	sys.stdout.write('\n')

if __name__ == "__main__":
	if len(sys.argv) == 2:
		print_thue_morse(int(sys.argv[1]))
	else:
		print_thue_morse(4)
