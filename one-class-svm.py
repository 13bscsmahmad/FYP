"""

This script trains a one-class SVM (support vector machine).
Input: libsvm format with only 0s


"""
# coding: utf-8
# In[29]:

from sklearn import svm
from sklearn.datasets import load_svmlight_file
from sklearn.externals import joblib

import pickle


# In[33]:
print "loading dataset..."
X_train, y_train = load_svmlight_file("train_numeric_svmLight.txt")


# In[34]:

clf = svm.SVC(verbose=3)
print "starting training..."
clf = clf.fit(X_train, y_train)
print "saving model..."
#s = pickle.dumps(clf)
joblib.dump(clf, 'one-class-svm.pkl') # to read back, clf = joblib.load('filename.pkl') 


# In[35]:

#load data to test

#X_test, y_test = load_svmlight_file("D:\\Documents\\FYP\\test_svmLight_2500.0.txt")


# In[37]:

#clf2 = pickle.loads(s)

#test model
#clf2.score(X_test, y_test)


# In[ ]:

#clf2.predict()

