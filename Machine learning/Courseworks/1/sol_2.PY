import numpy as np
import random


def learn_linear_regression(X, y, k, tau, lmbda):
    n,m=X.shape
    x_ones=np.ones((n,1))
    X_new=np.hstack([x_ones,X])
    beta=np.random.randn(m+1,1)
    prev_cost=float('inf')
    for i in range(k):
        y_pred=np.dot(X_new,beta)
        e=y_pred-y
        grad=np.dot(X_new.T,e)/n
        beta=beta-lmbda*grad
        cost = (1 / (2 * n)) * np.sum((y_pred - y)**2)
        new_cost=prev_cost-cost
        prev_cost=cost
        if(abs(new_cost)<tau):
            break
    return beta,cost