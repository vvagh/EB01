# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

""" Read CSV File """
data = pd.read_csv("Features.csv")
print(data.head())

""" Labels and Features """
# Labels = data which we want to predict (Y)
# Features = data which are used to predict labels (X)

y = data.relevance
X = data.drop('relevance', axis=1)

""" Splitting Data into Train & Test """
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print("\nX_train:\n")
print(X_train.head())
print(X_train.shape)

print("\nX_test:\n")
print(X_test.head())
print(X_test.shape)

