import os

fileOriginal_path = "../Dataset/test_numeric.csv"
filePCA_LIBSVM_path = "../Dataset/test_svmLightPCA_test_numeric.txt"

print "initializing..."

f = open(fileOriginal_path,"r") ##original file
#g = open(fileLIBSVM_path,"w") ##same data in svmLight format 

x_train=[] 
y_train=[]

count = 0

##the length of each line varies in training and testing files, the training files co
skip = 1

print "reading raw file..."

for i in f:
    if skip == 1:
    	skip = 0
    	continue

    data = [None] * 968 ##the test file contains 969 values in each line, 1 is removed in data, the id

    x = i.split(",")

    for j in range(1,969):
    	data[j-1] = x[j]

    mine = [None] * 968    

    line = ""

    for column in range(0,967):
    	if data[column] == '':	##assign all the features without any values with 0 value
    		data[column] = '0'
    	mine[column] = float(data[column])

 #   	line = line + (" "+ str(column)+":"+str(data[column]))

 #   line = line + "\n"

 #   if line == "\n":
 #   	line = ""
 #   	break
    x_train.append(mine)        


    #g.write(line)
    count += 1
    print ("Lines written: " + str(count))

print "written in svmLight and populated in x_train and y_train... \n "

####################################
print "IPCA starting... \n "

from sklearn.decomposition import IncrementalPCA
ipca = IncrementalPCA(n_components = 100, batch_size = 100000)
reduced = ipca.fit_transform(x_train)
print "IPCA finished... \n "
#########################################
print "storing in libSVM format... \n "
XXX = open(filePCA_LIBSVM_path,"w")  

for i in range(0,1183748): # samples in test file
    line = "" 
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
XXX.close()
fpn.close()
n.close()
XXX.close()
