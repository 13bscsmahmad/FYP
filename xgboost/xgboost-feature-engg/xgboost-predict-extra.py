'''
This script predicts using the trained xgboost model.
The xgboost model is supposed to be trained on the numeric features +
Faron's magic features.
'''

import pandas as pd
import numpy as np
import xgboost as xgb

MODEL_NAME = "xgboost-numeric-and-features-engineered-faron-model"
TEST_DATA = "../../Dataset/id-based-features-and-numeric-test.csv"

testing_dataset = pd.read_csv(TEST_DATA)
print("testing_dataset shape: ")
print(testing_dataset.shape)

print("Removing Id column...")
ids = testing_dataset.Id.ravel()
testing_dataset.drop('Id', 1) # drop the Id column from the dataframe

## Convert training_dataset to numpy array
testing_dataset = np.array(testing_dataset)
print("testing_dataset numpy array's shape:")
print(testing_dataset.shape)

# load model from file
print("Loading saved model...")
bst = xgb.Booster({'nthread':4}) #init model
bst.load_model(MODEL_NAME) # load data

#Data to test in DMatrix form
dtest = xgb.DMatrix(testing_dataset)

# make predictions for test data
print("Predicting...")
y_pred = bst.predict(dtest)
#predictions = [int(round(value)) for value in y_pred]

'''
The IDs are all stored in a single row. [1,2,4,7]. 
We will convert them into multiple rows [[1],[2],[4],[7]]
'''
IDs_in_height = np.array(ids)[np.newaxis].T
predictions_in_height = np.array(y_pred)[np.newaxis].T
finalMatrix = np.hstack((IDs_in_height, predictions_in_height)) # stack IDs and predictions horizontally

finalArray = np.asarray(finalMatrix) # convert numpy matrix to regular array

np.savetxt("submission.csv", finalArray, delimiter=",", header="Id,Response", fmt='%d')

print "Save successful"