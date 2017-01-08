"""

This script imputes (replaces) missing values with "0".

Input: .csv file with missing values
Output: .csv file with missing values replaced with "0"

"""

def checkMissing():
	test_numeric_imputed = open("test_numeric_imputed.csv", "r")
	rowNumber = 0

	for line in test_numeric_imputed:
		line_tokens = line.strip().split(",")
		for token in line_tokens:
			if token == "" or len(token) < 1:
				print "missing value found at row: ", rowNumber
				test_numeric_imputed.close()
				return

		rowNumber+=1
	print "No missing values!"
	print "Rows in file = ", rowNumber
	test_numeric_imputed.close()
	return
	
	
	

test_numeric = open("test_numeric.csv", "r")
test_numeric_imputed = open("test_numeric_imputed.csv", "w")


numberOfMissingVals = 0
rows = 0

for line in test_numeric:
	line_tokens = line.strip().split(",")
	for x in xrange(0,len(line_tokens)):
		if line_tokens[x] == "": #or len(line_tokens[x]) < 1:
			numberOfMissingVals+=1
			line_tokens[x] = "0" # replacing missing value with '0'
	test_numeric_imputed.write(",".join(str(x) for x in line_tokens)+'\n') # converting list to string for output
	#print line_tokens
	rows+=1

test_numeric.close()
test_numeric_imputed.close()

print "rows = ", rows
print "Initial number of missing values = ", numberOfMissingVals
checkMissing()

			
	
