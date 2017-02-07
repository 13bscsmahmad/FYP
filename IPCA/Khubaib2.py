def check():
	fopen = open("final.csv", "r")

	rows = 0
	number0s = 0
	number1s = 0

	header = fopen.readline().strip()
	rows+=1

	for line in fopen:
		tokens = line.strip().split(",")
		#print len(tokens)
		if tokens[969] == "0":
			number0s+=1
		elif tokens[969] == "1":
			number1s+=1

		rows+=1

	fopen.close()

	print "Number of 0s = ", number0s
	print "Number of 1s = ", number1s
	print "Number of rows = ", rows
	return


def main():
    
    file0s_path = "train_numeric_0s.csv"
    file1s_path = "train_numeric_1s.csv"
    fileFinal_path = "final.csv"

    fopen0s = open(file0s_path, "r")
    fopen1s = open(file1s_path, "r")

    lines = 0

    fopen = open(fileFinal_path, "w")

    # Remove header from buffers

    header = fopen0s.readline().strip()
    header = fopen1s.readline().strip()

    # Copy header row

    fopen.write(header+'\n')
    lines+=1

    # Alternate b/w 0s and 1s

    for x in range(0,1000):
    	# First copy row from 0s file
    	line = fopen0s.readline().strip()
    	#print line
    	fopen.write(line+'\n')
    	lines+=1
    	# Then copy row from 1s file
    	line = fopen1s.readline().strip()
    	fopen.write(line+'\n')
    	lines+=1

    	#myfile = open("final.csv","r+")
    print "Lines: ", lines
    fopen.close()
    fopen0s.close()
    fopen1s.close()

    check()

if __name__ == "__main__":
    main()