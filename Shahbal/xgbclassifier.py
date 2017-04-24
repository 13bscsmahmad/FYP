from xgboost import XGBClassifier 
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

train = pd.read_csv("/home/g13bscsmshahbal/scripts/balanced_train_joined.csv") #load dataframe train
train.fillna(0, inplace=True)

feats = np.setdiff1d(list(train.columns), ['Id','Response'])

X_train = np.array(train[feats])
y_train = train.Response.ravel()


test = pd.read_csv("/home/mma/MMA/FYP/Dataset/id-based-features-and-numeric-test.csv")
IDS = test.Id

feats = np.setdiff1d(list(test.columns), ['Id'])

X_test = np.array(test[feats])

prior = np.sum(y_train) / (1.*len(y_train))
model = XGBClassifier(seed=0, colsample_bytree=0.7, silent=1, subsample=0.1, learning_rate=0.1, objective='binary:logistic', max_depth=4, num_parallel_tree=1, min_child_weight=2, base_score=prior)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

pred = pd.DataFrame({'Id': IDS,
						'Response': y_pred})


pred = pred.set_index('Id')


pred.to_csv("pred_xgb_setparams.csv")

