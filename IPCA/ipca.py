runScript = 12 # run this script 12 times for 12,00,000 samples
increment = 100000 # constant, used at the end of each loop
scriptCounter = 0 # variable. Used at the end of each loop
init = 0 # variable, used to control inner loop
final = 100000 # variable, used to control inner loop


fileOriginal_path = "../Dataset/train_numeric.csv"
fileLIBSVM_path = "../Dataset/train_numeric_svmLight.txt"
filePCA_LIBSVM_path = str(scriptCounter) + "_train_svmLightPCA_train_numeric.txt"

print "initializing..."

f = open(fileOriginal_path,"r") ##original file
g = open(fileLIBSVM_path,"w") ##same data in svmLight format 

x_train=[] 
y_train=[]

#a = f.readlines()
count = 0

##the length of each line varies in training and testing files, the training files co
skip = 1

print "reading raw file..."

for i in f:
	if skip == 1:
		skip = 0
		continue

	data = ['none'] * 968 ##the training file contains 970 values in each line, 2 are removed in data, the id and the response

	x = i.split(",")
	response = x[969].strip()
	for j in range(1,969):
		data[j-1] = x[j]

	y_train.append(int(response))
	mine = [None] * 968    
	line = ""
	for i in range(0,968):
		if data[i] == '' or data[i] == '0':	##assign all the features without any values with 0 value
			data[i] = '0'
		mine[i] = float(data[i])
		line = line + (" "+ str(i)+":"+str(data[i]))

	line = line + "\n"

	if line == "\n":
		line = ""
		break
	x_train.append(mine)        
    

	g.write(line)
	count += 1

print "written insvmLight and populated in x_train and y_train... \n "

####################################
print "IPCA starting... \n "

from sklearn.decomposition import IncrementalPCA
ipca = IncrementalPCA(n_components = 100, batch_size = 100000)
reduced = ipca.fit_transform(x_train)
##ipca.transform(x_train)
print "IPCA finished... \n "
#########################################
print "storing in libSVM format... \n "
XXX = open(filePCA_LIBSVM_path,"w")  

for i in range(0,1183747): # originally, 1183747 (for complete dataset)
    line = ""
    line = line + str(y_train[i])
    t_line = ""

    for j in range(0,100):
        t_line = t_line + " "+ str(j) + ":" + str(reduced[i][j])
    
    line = line + t_line + "\n"
    XXX.write(line)
##############################################################
n = open(filePCA_LIBSVM_path,'r')
a = n.readline()
print a
#####################################################3
fpn=open(fileOriginal_path,'r')
frn=fpn.readline()
print frn
####################################
f.close()
g.close()
fpn.close()
n.close()
XXX.close()


