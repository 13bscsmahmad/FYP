f = open("test_numeric_prediction.txt","r")

total_responses = 0
total_1s = 0

for line in f:
	lineTokens = line.strip().split(",")
	print len(lineTokens)
	if lineTokens[1] == "1":
		total_1s+=1
	total_responses+=1

print "1s: " , total_1s
print "total responses = ", total_responses
