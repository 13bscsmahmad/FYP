"""
This script uses a pre-built classifier to predict classes of samples.

Input:
1) path to model
2) path to .csv file which contains the samples whose class is to be predicted

Output: File that contains Id,Response for each sample in the input file, where Response contains the 
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_svmlight_file
from sklearn.externals import joblib
import numpy as np

clf = joblib.load('randomforest.pkl')

originalFile = open("../test_numeric_imputed.csv", "r")
newFile = open("test_numeric_prediction.txt", "w")

newFile.write("Id,Response"+'\n')

ids = [] # to store ids in order
predictionLabels = [] # to store prediction class

lineNumber = 0

for line in originalFile:

	if lineNumber == 0: # skip header row
		lineNumber+=1		
		continue

	tokenList = line.strip().split(",")
	currentID = tokenList.pop(0) #remove id from 0th column
	#ids.append(currentID) #  and append to id list
	print "Working with ID: ", currentID
	prediction = clf.predict(np.asarray(tokenList).reshape(1,-1)) # use the remaining items to make a prediction
	#predictionLabels.append(prediction) # append prediction to prediction list

	newFile.write(str(currentID)+","+ str([int(i) for i in prediction.tolist()]).strip('[]')+"\n") # convert float numpy to int list, then to string, then add \n, and write to file

	lineNumber+=1

#if len(ids) == len(predictionLabels): # ensure that we have predictions for all ids
#	for i in xrange(0,len(ids)):
#		newFile.write(str(ids[i])+","+str(predictionLabels[i]+"\n"))

originalFile.close()
newFile.close()

"""
lineNumber = 0
for line in originalFile:
	if lineNumber == 0:
		lineNumber+=1		
		continue
		
	predictionSampleTokens = line.split(",", 1) #split only once.
	predictionSampleID = predictionSampleTokens[0] # has the ID
	predictionSample = predictionSampleTokens[1] # has the rest of the comma separated data
	myworkinglist = predictionSample.split(",")
	myfinallist = [float(i) for i in myworkinglist]
	print myfinallist
	prediction = clf.predict(myfinallist)

	newFile.write(predictionSampleID+":"+prediction[0])	
	lineNumber+=1

originalFile.close()
newFile.close()
"""
