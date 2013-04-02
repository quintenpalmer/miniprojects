#!/usr/bin/env python

from rlist import randList
from ms import ms
from array_printer import print_array

with open('../size.txt','r') as f:
	size = int(f.readline().strip())
pre_sort = randList(size)
post_sort = ms(pre_sort)

print_array(pre_sort)
print_array(post_sort)
