#!/usr/bin/env python
import time
import sys

st = "Happy Easter!"
colors = ['31','33','32','36','34','35']
i = 0

def increment_i():
	global i
	i = i+1 if i < 5 else 0

for tmp in range(18):
	for j in range(6):
		increment_i()
		sys.stdout.write("\33["+colors[i]+"m"+st+"\33[0m\n")
	time.sleep(1.0/4)
	increment_i()
	sys.stdout.write("\33[6A\r")
sys.stdout.write("\n"*6)
