#!/usr/bin/env python
import time
import sys

f = open('../settings.txt','r')
num = int(f.readline().strip())
wait_time = float(f.readline().strip())/1000

for i in range(num+1):
	sys.stdout.write('\r'+str(i)+'%  ')
	sys.stdout.flush()
	time.sleep(wait_time)
sys.stdout.write('\n')
