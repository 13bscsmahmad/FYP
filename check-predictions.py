#!/usr/bin/env python
import sys

############

print "checking using simple fopen() function"
print "======================================\n"

f = open(sys.argv[1], "r")
count0s = 0
count1s = 0
lines = 0

for line in f:
	tokens = line.strip().split(",")
	if tokens[1] == "0":
		count0s += 1
	elif tokens[1] == "1":
		count1s += 1

	lines += 1

print "Lines read: ", lines
print "0s in file: ", count0s
print "1s in file: ", count1s

f.close()

#############

print "Checking using pandas..."
print "========================\n"
import pandas as pd

fi = pd.read_csv(sys.argv[1])
print "0s in dataset"
print fi.loc[fi["Response"]==0]
print "1s in dataset"
print fi.loc[fi["Response"]==1]


