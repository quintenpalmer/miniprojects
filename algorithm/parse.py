#!/usr/bin/env python
import sys
import re

indent_level = 0
indentStr = '    '
delim = "QDELIMSEQUENCE"

def write_line(line):
	outLine = get_indent()
	outLine += line
	print(outLine)
def minus_indent():
	global indent_level
	indent_level -= 1
def plus_indent():
	global indent_level
	indent_level += 1
def get_indent():
	outStr = ''
	for i in range(0,indent_level):
		outStr += indentStr
	return outStr

arg = sys.argv[1]
arg = re.sub(",",","+delim,arg)
arg = re.sub(r"([{\(\[])",r"\1"+delim,arg)
arg = re.sub(r"([}\)\]])",delim+r"\1",arg)
arg = re.sub(" +"," ",arg)
arg = re.sub(delim+" ",delim,arg)
arg = arg.split(delim)
for a in arg:
	if re.findall(r"[\)\]}]",a):
		minus_indent()
	write_line(a)
	if re.findall(r"[\(\[{]",a):
		plus_indent()
