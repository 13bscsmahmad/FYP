def check(file_0s, file_1s):
	fopen0s = open(file_0s, "r")
	fopen1s = open(file_1s, "r")

	numberOf0s = 0
	numberOf1s = 0
	rowsIn0file = 0
	rowsIn1file = 0

	header0s = fopen0s.readline().strip()
	header1s = fopen1s.readline().strip()
	rowsIn0file+=1
	rowsIn1file+=1

	for line in fopen0s:
		lineTokens = line.strip().split(",")
		#print len(lineTokens)
		if (lineTokens[969]=="0"):
			numberOf0s+=1
		rowsIn0file+=1

	fopen0s.close()

	for line in fopen1s:
		lineTokens = line.strip().split(",")
		if (lineTokens[969]=="1"):
			numberOf1s+=1
		rowsIn1file+=1

	fopen1s.close()

	print "Rows in 0s = ", rowsIn0file
	print "Number of 0s in 0s file = ", numberOf0s
	print "Rows in 1s = ", rowsIn1file
	print "Number of 1s in 1s file = ", numberOf1s




def main():
    
    originalFile_path = "..//Dataset/train_numeric.csv"
    file0s_path = "train_numeric_0s.csv"
    file1s_path = "train_numeric_1s.csv"
    
    fopen = open(originalFile_path, "r") # original file    
    file0s = open(file0s_path, "w") # to store all 0s
    file1s = open(file1s_path, "w") # to store all 1s

    rowNumber = 0

    headerRow = fopen.readline().strip()
    file0s.write(headerRow + '\n') # copy header row. Since header row did not have a \n due to strip(), we add one ourself 
    file1s.write(headerRow + '\n') # copy header row
    rowNumber+=2



    for line in fopen:

        lineTokens = line.strip().split(",")
        #print len(lineTokens)
        if (lineTokens[969]=="0"):
            file0s.write(line) # line variable already has a \n from when it was read from file, so no need to add it ourself
        elif (lineTokens[969]=="1"):
            file1s.write(line) # line variable already has a \n from when it was read from file, so no need to add it ourself
        else:
            "error at row: ", rowNumber
            exit()
            rowNumber+=1

            file0s.close()
            file1s.close()
            fopen.close()

    check(file0s_path, file1s_path)

if __name__ == "__main__":
    main() 


