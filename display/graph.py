#!/usr/bin/env python
import sys

def graph(width,height,pairs,wscale=1,hscale=1):
	height = 2*(int(height/float(hscale)))
	width = int((width+1)/wscale)
	spairs = []
	for i in xrange(0,len(pairs)):
		spairs.append([])
		spairs[i].append(1)
		spairs[i].append(1)
		spairs[i].append(pairs[i][2])
		spairs[i].append(pairs[i][3])
	for i in xrange(0,len(pairs)):
		spairs[i][0] = (pairs[i][0]/float(hscale))
		spairs[i][1] = (pairs[i][1]/float(hscale))
	out = []
	for i in xrange(0,height):
		out.append([])
		out[i].append(str(i*hscale)+'\t')
		for j in xrange(1,width):
			out[i].append('\33[30m.\33[0m')

	for i in xrange(1,len(spairs)+1):
		for pair in spairs:
			point = int(pair[0]+i*pair[1])
			move = int(i/wscale)+1
			out[0][move] = str(spairs[i-1][3])
			if out[point][move] == '\33[30m.\33[0m':
				out[point][move] = pair[2]
			else:
				out[point][move]+=pair[2]

	for i in xrange(height-1,-1,-1):
		sys.stdout.write('\r')
		for j in xrange(0,width):
			sys.stdout.write(out[i][j])
		sys.stdout.write('\n')

colors = [35,34,36,32,33,31]
pairs = [
[40,45,'\33['+str(colors[0])+'ma\33[0m',1],
[70,40,'\33['+str(colors[1])+'mb\33[0m',4],
[90,35,'\33['+str(colors[2])+'mc\33[0m',6],
[120,30,'\33['+str(colors[3])+'md\33[0m',10],
[160,30,'\33['+str(colors[4])+'me\33[0m',15],
[200,30,'\33['+str(colors[5])+'mf\33[0m',20]]
w = 0
for pair in pairs:
	w = max(w,pair[0])
l = len(pairs)
graph(l,w,pairs,wscale=.1,hscale=11)
lowest = 50
highest = 160
dif = (highest - lowest)/6
markers = []
for i in xrange(0,6):
	markers.append('\33['+str(colors[i])+'m')
def colorVal(val):
	out = ''
	tmp = int(round((val - lowest)/float(dif)))
	out += '\33['+str(colors[min(tmp,5)])+'m'+str(val)+'\33[0m'
	return out
numUsr = 5
numPlans = 6
sys.stdout.write('gb\t')
for i in xrange(1,numUsr+1):
	sys.stdout.write(str(i)+' ppl\t')
sys.stdout.write('\n')
for j in xrange(0,numPlans):
	sys.stdout.write(str(pairs[j][3])+'\t')
	for i in xrange(1,numUsr+1):
		val = (pairs[j][0]+pairs[j][1]*i)/i
		sys.stdout.write('$'+colorVal(val)+'\t')
	sys.stdout.write('\n')
'''
for i in xrange(1,numUsr+1):
	print i, "users"
	print 'gb\ttotal\tper person'
	for j in xrange(0,numPlans):
		total = pairs[j][0]+pairs[j][1]*i
		per = (pairs[j][0]+pairs[j][1]*i)/i
		print pairs[j][3],'\t',colorVal(total),'\t',colorVal(per)
'''
