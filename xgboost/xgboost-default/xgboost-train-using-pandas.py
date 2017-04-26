'''
This script uses the dataset train_numeric.
Unlike the other script,
this does NOT split the data into 70:30 train:test.
It trains the COMPLETE train_numeric dataset through the xgboost algorithm,
and saves the model.

Uses pandas library
'''

import numpy as np
import xgboost as xgb
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd

#TRAIN_DATA = "../../Dataset/id-based-features-and-numeric-train.csv"
TRAIN_DATA = "../../Dataset/train_numeric.csv"
TEST_DATA = "../../Dataset/test_numeric.csv"

dataset = pd.read_csv(TRAIN_DATA)
print("dataset shape: ")
print(dataset.shape)

# Get labels and ids from the file
y = dataset.Response.ravel()
ids = dataset.Id.ravel()

# Drop Id and Response columns from the training dataset
dataset = dataset.drop('Id', 1)
dataset = dataset.drop('Response', 1)


# Convert dataset to numpy array
dataset = np.array(dataset)

#print shape of training_dataset
print("dataset shape: ")
print(dataset.shape)

dtrain = xgb.DMatrix(dataset, label=y)
print ("training data...")

xgb_params = {
    'max_depth':3,
    'learning_rate':0.1,
    'n_estimators':100,
    'silent':True,
    'objective':'binary:logistic',
    'nthread':-1,
    'gamma':0,
    'min_child_weight':1,
    'max_delta_step':0,
    'subsample':1,
    'colsample_bytree':1,
    'colsample_bylevel':1,
    'reg_alpha':0,
    'reg_lambda':1,
    'scale_pos_weight':1,
    'base_score':0.5,
    'seed':0,
    'missing':None
}

#Train the model
trained_model = xgb.train(dtrain=dtrain, params=xgb_params, verbose_eval=True)

#Save the model
trained_model.save_model("xgboost-numeric-pandas")

print("Saved model.")

##########################################################################

print("Loading prediction data...")
dataset = pd.read_csv(TEST_DATA)

# Get Ids
ids = dataset.Id.ravel()

# Drop IDs
dataset = dataset.drop('Id', 1)
dataset = np.array(dataset)
dataset = xgb.DMatrix(dataset)

# make predictions for test data
print("Predicting...")
y_pred = trained_model.predict(dataset)

pred = pd.DataFrame({'Id': IDS, 'Response': y_pred})


pred = pred.set_index('Id')


pred.to_csv("pred_train_numeric.csv")





