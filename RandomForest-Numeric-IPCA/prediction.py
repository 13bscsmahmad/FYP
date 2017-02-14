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

originalFile = open("../Dataset/test_numeric.csv", "r") # to get ID number of component
PCAfile = open("../IPCA/test_svmLightPCA_test_numeric.txt", "r") # to get feature values
newFile = open("test_numeric_prediction_PCA.txt", "w") # submission file

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

    PCARow = PCAfile.readline()
    PCATokenListWithSerialNumber = PCARow.strip().split(" ") # split feature values which separated by whitespace
    PCATokenListWithoutSerialNumber = []
    for tokenNumber in range(0, len(PCATokenListWithSerialNumber)):
        tempTokens = PCATokenListWithSerialNumber[tokenNumber].split(":") # split so the [0] has serial number, [1] has feature values
        PCATokenListWithoutSerialNumber.append(float(tempTokens[1]))

    ####################################################################################################################
    #ids.append(currentID) #  and append to id list
    print "Working with ID: ", currentID
    prediction = clf.predict(np.asarray(PCATokenListWithoutSerialNumber).reshape(1,-1)) # use the remaining items to make a prediction
    #predictionLabels.append(prediction) # append prediction to prediction list

    newFile.write(str(currentID)+","+ str([int(i) for i in prediction.tolist()]).strip('[]')+"\n") # convert float numpy to int list, then to string, then add \n, and write to file
    ####################################################################################################################

    lineNumber+=1
    
    del PCATokenListWithSerialNumber[:]
    del PCATokenListWithoutSerialNumber[:]
    del tempTokens[:]

PCAfile.close()
originalFile.close()
newFile.close()
