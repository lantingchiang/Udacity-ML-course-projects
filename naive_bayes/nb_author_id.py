#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 
    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
sys.path.append("../tools/")
from time import time
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB


"""
features_train and features_test are the features for the training
and testing datasets, respectively
labels_train and labels_test are the corresponding item labels
"""
features_train, features_test, labels_train, labels_test = preprocess()

classifier = GaussianNB()
t0 = time()  # time elapsed since epoch
classifier.fit(features_train, labels_train)
print("training time:", round(time() - t0, 3), "s")
t1 = time()
prediction = classifier.predict(features_test)
print("training time:", round(time()-t1, 3), "s")
accuracy = classifier.score(prediction, labels_test)
print(accuracy)

