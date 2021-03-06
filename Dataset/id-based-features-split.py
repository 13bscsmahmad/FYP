# -*- coding: utf-8 -*-
'''
Input: This script takes a csv file which contains id, response, all numeric features, start_time, feature1, feature2, feature3, and feature4
created by the script "id-based-features.py".

Processing: Splits the input into separate train and test files.

Output: train file which contains id, response, start_time, numeric features, feature1, feature2, feature3, feature4
        test file which containts id, numeric features, start_time, feature1, feature2, feature3, feature4
'''
import pandas as pd
import numpy as np
import xgboost as xgb

#DATA_DIR = "../input"

# ID_COLUMN = 'Id'
# TARGET_COLUMN = 'Response'
#
# SEED = 0
# CHUNKSIZE = 50000
# NROWS = 250000

# SOURCE_FILENAME="id-based-features.csv"
SOURCE_FILENAME="id-based-features-and-numeric-features.csv"
DESTINATION_FILENAME_TRAIN="id-based-features-and-numeric-train.csv"
DESTINATION_FILENAME_TEST="id-based-features-and-numeric-test.csv"

# train = pd.read_csv(TRAIN_NUMERIC, usecols=[ID_COLUMN, TARGET_COLUMN], nrows=NROWS)
# test = pd.read_csv(TEST_NUMERIC, usecols=[ID_COLUMN], nrows=NROWS)

dataset = pd.read_csv(SOURCE_FILENAME, index_col=0)
print dataset

#print dataset.loc[dataset['Response'] == np.NaN]

#get train_dataset
train_dataset = dataset.loc[pd.notnull(dataset['Response'])] # all those columns where Response!=NaN
train_dataset.Response = train_dataset.Response.astype(int) # convert Response to int (originally, float)

# Store Ids and Response
idr = train_dataset[['Id','Response']]
# Drop Ids and Response from train_dataset
train_d2 = train_dataset.drop(['Id', 'Response'], axis=1)
# Concatenate the 2 dataframes so that the final dataframe has Id, Response, features
train_d3 = pd.concat([idr, train_d2], axis=1)

# Save the final dataframe
print ("train_dataset saving...")
train_dataset.to_csv(DESTINATION_FILENAME_TRAIN, index=False)
print ("train_dataset saved!")


#get test_dataset
test_dataset = dataset.loc[pd.isnull(dataset['Response'])] # all those columns where Response=NaN
test_dataset = test_dataset.drop('Response', 1) # drop Response column
print ("test_dataset saving...")
test_dataset.to_csv(DESTINATION_FILENAME_TEST, index=False)
print ("test_dataset saved!")