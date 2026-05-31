import numpy as np
import random

def data_set(n,m,sigma):
    np.random.seed(40)
    X_features=np.random.randn(n,m)
    ones_column = np.ones((n, 1))
    X = np.hstack((ones_column, X_features))
    e=np.random.randn(n,1)*sigma
    ran_beta=np.random.randn(m+1,1)
    y=np.dot(X,ran_beta) + e
    return X, y, ran_beta