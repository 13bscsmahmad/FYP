# -*- coding: utf-8 -*-
"""
@author: Faron
"""
import pandas as pd
import numpy as np
import xgboost as xgb

DATA_DIR = "../../Dataset"

ID_COLUMN = 'Id'
TARGET_COLUMN = 'Response'

SEED = 0
# CHUNKSIZE = 50000
# NROWS = 250000

TRAIN_NUMERIC = "{0}/id-based-features-and-numeric-train.csv".format(DATA_DIR)
TEST_NUMERIC = "{0}/id-based-features-and-numeric-test.csv".format(DATA_DIR)


train = pd.read_csv(TRAIN_NUMERIC)
test = pd.read_csv(TEST_NUMERIC)

#print(train_test)

features = np.setdiff1d(list(train.columns), [TARGET_COLUMN, ID_COLUMN])

y = train.Response.ravel()
train = np.array(train[features])

print('train: {0}'.format(train.shape))
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


dtrain = xgb.DMatrix(train, label=y)
res = xgb.cv(xgb_params, dtrain, num_boost_round=10, nfold=4, seed=0, stratified=True,
             early_stopping_rounds=1, verbose_eval=1, show_stdv=True)

cv_mean = res.iloc[-1, 0]
cv_std = res.iloc[-1, 1]

print('CV-Mean: {0}+{1}'.format(cv_mean, cv_std))

booster_model = xgb.train(xgb_params, dtrain)

'''
Predict and write to file
'''

iidd = test_data.Id.ravel()
test = test.drop('Id', 1)
test = np.array(test[features])
dtest = xgb.DMatrix(test)
y_pred = booster_model.predict(dtest) # returns numpy array

predictions = [int(round(value)) for value in y_pred]
IDs_in_height = np.array(iidd)[np.newaxis].T
predictions_in_height = np.array(predictions)[np.newaxis].T
finalMatrix = np.hstack((IDs_in_height, predictions_in_height))
finalArray = np.asarray(finalMatrix)
np.savetxt("submission-faron_exact-xgboost-pandas.csv", finalArray, delimiter=",", header="Id,Response", fmt='%d')
print "Save successful"