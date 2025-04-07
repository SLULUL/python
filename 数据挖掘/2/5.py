import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

digits = load_digits()
X, Y = digits.data, digits.target
X_train, X_test, Ytrain, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=420)

gnb = GaussianNB().fit(X_train, Ytrain)

prob = gnb.predict_proba(X_test)
print(prob)
