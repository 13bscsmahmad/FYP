'''
This script will read the split files id-based-features-train.csv and
id-based-features-test.csv

The features in the training file include all the numeric features + 5 of Faron's engineered features.

It will then train an xgboost model.

'''

import pandas as pd
import numpy as np
import xgboost as xgb

DATA_DIR = "../../Dataset"

ID_BASED_AND_NUMERIC_FEATURES_TRAIN = "../../Dataset/id-based-features-train.csv"

# Read train dataset
training_dataset = pd.read_csv(ID_BASED_AND_NUMERIC_FEATURES_TRAIN)

# Get labels and ids from the file
y = training_dataset.Response.ravel()
ids = training_dataset.Id.ravel()

# Drop Id and Response columns from the training dataset
training_dataset = training_dataset.drop('Id', 1)
training_dataset = training_dataset.drop('Response', 1)

# Convert training_dataset to numpy array
training_dataset = np.array(training_dataset)

#print shape of training_dataset
print("training_dataset shape: ")
print(training_dataset.shape)

prior = np.sum(y) / (1.*len(y))

xgb_params = {
    'seed': 0,
    'colsample_bytree': 0.7,
    'silent': 1,
    'subsample': 0.7,
    'learning_rate': 0.1,
    'objective': 'binary:logistic',
    'max_depth': 4,
    'num_parallel_tree': 1,
    'min_child_weight': 2,
    'eval_metric': 'auc',
    'base_score': prior
}

dtrain = xgb.DMatrix(training_dataset, label=y)

print ("training data...")

#Train the model
trained_model = xgb.train(xgb_params, dtrain, verbose_eval=True)

#Save the model
trained_model.save_model("xgboost-numeric-and-features-engineered-faron-model")

print("Saved model.")