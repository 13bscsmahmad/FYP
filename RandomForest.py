
# coding: utf-8

# In[29]:

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_svmlight_file
import pickle


# In[33]:

X_train, y_train = load_svmlight_file("D:\\Documents\\FYP\\train_svmLight_2500.0.txt")


# In[34]:

clf = RandomForestClassifier(n_estimators=10, max_depth=10)
clf = clf.fit(X_train, y_train)
s = pickle.dumps(clf)


# In[35]:

#load data to test

X_test, y_test = load_svmlight_file("D:\\Documents\\FYP\\test_svmLight_2500.0.txt")


# In[37]:

clf2 = pickle.loads(s)

#test model
clf2.score(X_test, y_test)


# In[ ]:

clf2.predict()

