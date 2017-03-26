import numpy
import xgboost
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# load data
# dataset = numpy.loadtxt('pima-indians-diabetes.csv', delimiter=",")

dataset = numpy.genfromtxt('../Dataset/train_numeric.csv', delimiter=",", skip_header=1)

# split data into X and y
# X = dataset[:,0:8]
# Y = dataset[:,8]

X = dataset[:,1:968]
Y = dataset[:,969]

# split data into train and test sets
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

# fit model to training data
model = xgboost.XGBClassifier(silent=False)
model.fit(X_train, y_train)

print(model)

# make predictions for test data
y_pred = model.predict(X_test)
predictions = [round(value) for value in y_pred]

# evaluate predictions
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

#save the model
model.save_model("xgboost_numeric_train_001")
print("Saved model.")

