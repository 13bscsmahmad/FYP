# Train XGBoost model, save to file using pickle, load and make predictions
import numpy
from numpy import loadtxt
import xgboost as xgb
import pickle
from sklearn import model_selection
from sklearn.metrics import accuracy_score

MODEL_NAME = "xgboost-features-engineered-faron-model"
TEST_DATA = "../../Dataset/id-based-features-test.csv"
# load data
#dataset = loadtxt('pima-indians-diabetes.csv', delimiter=",")

dataset = numpy.genfromtxt(TEST_DATA, delimiter=",", skip_header=1)

IDs = dataset[:,0] # store all component IDs
testset = dataset[:,1:5] # test values
 
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
bst = xgb.Booster({'nthread':4}) #init model
bst.load_model("xgboost-features-engineered-faron-model") # load data

#Data to test in DMatrix form
dtest = xgb.DMatrix(testset)

# make predictions for test data
y_pred = bst.predict(dtest)
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