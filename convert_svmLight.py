
f = open("train_numeric.csv","r") ##original file
g = open("train_numeric_svmLight","w") ##same data in svmLight format 


a = f.readlines()
count = 0

##the length of each line varies in training and testing files, the training files co
skip = 1
for i in a:
	if skip == 1:
		skip = 0
		continue
	
	data = ['none'] * 968 ##the training file contains 970 values in each line, 2 are removed in data, the id and the response

	x = i.split(",")
	response = x[969].strip()
	for j in range(1,969):
		data[j-1] = x[j]


	line = ""
	line = line + (str(response))
	for i in range(0,968):
		if data[i] == '':	##skip all the features without any values and with 0 value
			data[i] = '0'
			continue
		line = line + (" "+ str(i)+":"+str(data[i]))
	
	line = line + "\n"

	if line == "\n":
		line = ""
		break

	g.write(line)
	count += 1


print count 
