# Train XGBoost model, save to file using pickle, load and make predictions
import numpy
from numpy import loadtxt
import xgboost
import pickle
from sklearn import model_selection
from sklearn.metrics import accuracy_score
# load data
#dataset = loadtxt('pima-indians-diabetes.csv', delimiter=",")

dataset = numpy.genfromtxt('../Dataset/test_numeric.csv', delimiter=",", skip_header=1) # only using to retrieve IDs. TODO: Get IDs from original submission.csv for lower mem. footprint.

IDs = dataset[:,0] # store all component IDs

testset = numpy.genfromtxt('../Dataset/test_numeric.csv', delimiter=",")
test_set = testset[:,0:99] # test values
 
# # split data into train and test sets
# seed = 7
# test_size = 0.33
# X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=test_size, random_state=seed)
# # fit model no training data
# model = xgboost.XGBClassifier()
# model.fit(X_train, y_train)
# # save model to file
# pickle.dump(model, open("pima.pickle.dat", "wb"))

# some time later...

# load model from file
loaded_model = pickle.load(open("xgboost_complete_numeric_train_PC-100_001-default", "rb"))
# make predictions for test data
y_pred = loaded_model.predict(test_set)
predictions = [int(round(value)) for value in y_pred]

'''
The IDs are all stored in a single row. [1,2,4,7]. 
We will convert them into multiple rows [[1],[2],[4],[7]]
'''
IDs_in_height = numpy.array(IDs)[numpy.newaxis].T
predictions_in_height = numpy.array(predictions)[numpy.newaxis].T
finalMatrix = numpy.hstack((IDs_in_height, predictions_in_height)) # stack IDs and predictions horizontally

finalArray = numpy.asarray(finalMatrix) # convert numpy matrix to regular array

numpy.savetxt("submission.csv", finalArray, delimiter=",", header="Id,Response", fmt='%d')

print "Save successful"


# evaluate predictions
#accuracy = accuracy_score(y_test, predictions)
#print("Accuracy: %.2f%%" % (accuracy * 100.0))


# load data
# dataset = numpy.loadtxt('pima-indians-diabetes.csv', delimiter=",")

#dataset = numpy.genfromtxt('../Dataset/test_numeric.csv', delimiter=",", skip_header=1)