import numpy as np
import random
import math

def logistic_regression(theta,n,m):
    np.random.seed(40)
    X_features=np.random.randn(n,m)
    ones=np.ones((n,1))
    Beta=np.random.randn(m+1,1)
    X=np.hstack((ones,X_features))
    prob=1/(1+np.exp(-1*(X@Beta)))
    Y=(prob > 0.5).astype(int)
    ran=np.random.rand(n,1)
    noise=Y ^ (ran<theta)
    return X,Y,Beta

if __name__ == "__main__":
    n=int(input("Enter the number of rows :"))
    m=int(input("Enter the number of column :"))
    theta=float(input("Enter the Value of theta:"))
    X,Y,beta=logistic_regression(theta,n,m)
    print("X [array of independent variable values] :\n",X,"\n")
    print("Y [array of dependent variable values] :\n",Y,"\n")
    print("Array of Beta Values:\n",beta,"\n")