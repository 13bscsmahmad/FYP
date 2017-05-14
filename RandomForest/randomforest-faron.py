from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_svmlight_file
from sklearn.externals import joblib
import pandas as pd
import numpy as np

import pickle

TRAIN_DATASET = "../Dataset/id-based-features-and-numeric-train.csv"
TEST_DATASET = "../Dataset/id-based-features-and-numeric-test.csv"
MODEL_NAME = "random-forest-numeric-and-faron.model"

f = pd.read_csv(TRAIN_DATASET)
y = f.Response.ravel()
f = f.drop('Response', 1)
ids = f.Id.ravel()
f = f.drop('Id', 1)

f = np.array(f)

model = RandomForestClassifier(verbose=3, n_jobs=-1)
print "starting training..."
model = model.fit(f, y)

print "saving model..."
#s = pickle.dumps(clf)
joblib.dump(model, MODEL_NAME) # to read back, clf = joblib.load('filename.pkl') 

# predict...

print("Saved model. Loading testset...")

g = pd.read_csv(TEST_DATASET)
ids = g.Id.ravel()
g = g.drop('Id', 1)
g = np.array(g)

print "predicting..."
y_pred = model.predict(g)
print "predictions made. Processing and saving..."

predictions = [int(round(value)) for value in y_pred]
IDs_in_height = np.array(ids)[np.newaxis].T
predictions_in_height = np.array(predictions)[np.newaxis].T
finalMatrix = np.hstack((IDs_in_height, predictions_in_height))
finalArray = np.asarray(finalMatrix)
np.savetxt("submission-numeric-faron-randomforest-pandas.csv", finalArray, delimiter=",", header="Id,Response", fmt='%d')
print "Save successful"