"""
This Python script splits LIBSVM dataset into 2 files:
	1) all positives
	2) all negatives
"""

f = open("train_svmLight.txt","r")
x = open("total_ones.txt","w")
y = open("total_zero.txt","w")

count = 0
positive = 0
negative = 0

a = 0
for a in range(1183748):
	j = f.readline()
	i = j.split(" ")
	count += 1
	if i[0].strip() is '1':	
		x.write(j)
		positive += 1
	if i[0].strip() is '0':
		y.write(j)
		negative += 1
	if i[0].strip() is not '1' and i[0].strip() is not '0':
		print i
	#print i[969]

print i
print count
print "positives: ", positive
print "negatives: ", negative
