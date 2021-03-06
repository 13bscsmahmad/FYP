'''
This script uses the dataset train_numeric.
Unlike the other script,
this does NOT split the data into 70:30 train:test.
It trains the COMPLETE train_numeric dataset through the xgboost algorithm,
and saves the model.

'''

import numpy
import xgboost
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle

TRAIN_DATASET = "../../Dataset/train_numeric.csv"
MODEL_NAME = "numeric_train_sklearn_xgboost.model"
# load data
# dataset = numpy.loadtxt('pima-indians-diabetes.csv', delimiter=",")

dataset = numpy.genfromtxt(TRAIN_DATASET, delimiter=",", skip_header=1)

# split data into X and y
# X = dataset[:,0:8]
# Y = dataset[:,8]

X = dataset[:,1:968]
Y = dataset[:,969]

# # split data into train and test sets
# seed = 7
# test_size = 0.33
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

# fit model to training data
model = xgboost.XGBClassifier(silent=False)
model.fit(X, Y)

print(model)

# make predictions for test data
# y_pred = model.predict(X_test)
# predictions = [int(round(value)) for value in y_pred]

# evaluate predictions
# accuracy = accuracy_score(y_test, predictions)
# print("Accuracy: %.2f%%" % (accuracy * 100.0))

#save the model
pickle.dump(model, open(MODEL_NAME, "wb"))
print("Saved model.")

