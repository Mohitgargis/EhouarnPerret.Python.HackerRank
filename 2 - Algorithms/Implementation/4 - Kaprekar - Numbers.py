#!/bin/python3

import sys
import math

def digits(n):
	return int(math.log10(n)) + 1

p = int(input().strip()) #lower bound
q = int(input().strip()) #upper bound

count = 0

for n in range(p, q + 1):
	n2 = n**2
	powdig = pow(10, digits(n))
	l = (n2 % powdig)
	r = (n2 // powdig)
	if ((l + r) == n):
		print (n, end=" ")
		count = count + 1
if (count == 0):
	print("INVALID RANGE")