#!/usr/bin/env python

from subprocess import check_output
import sys

if len(sys.argv) == 2 and sys.argv[1] == 'c':
	check_output(['gcc','-lm','ami.c'])
sys.stdout.write(check_output(['./a.out']))
