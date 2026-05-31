import numpy as np
import random

class Models:
    def __init__(self,n,m):
        self.n=n
        self.m=m

    def __str__(self):
        return f"Data:{n} rows {m} columns."

    def linear_regreion(self,sigma):
        self.sigma=sigma
        np.random.seed(40)
        self.X_features=np.random.randn(self.n,self.m)
        self.ones_column = np.ones((self.n, 1))
        self.X = np.hstack((self.ones_column, self.X_features))
        self.e=np.random.randn(self.n,1)*self.sigma
        self.ran_beta=np.random.randn(self.m+1,1)
        self.y=np.dot(self.X,self.ran_beta) + self.e
        return self.X, self.y

    def logistic_regression(self,theta):
        self.theta=theta
        np.random.seed(40)
        self.X_features=np.random.randn(self.n,self.m)
        self.ones=np.ones((self.n,1))
        self.Beta=np.random.randn(self.m+1,1)
        self.X=np.hstack((self.ones,self.X_features))
        self.prob=1/(1+np.exp(-1*(self.X@self.Beta)))
        self.Y=(self.prob > 0.5).astype(int)
        self.ran=np.random.rand(self.n,1)
        self.noise=self.Y ^ (self.ran<self.theta)
        return self.X,self.Y

class Learn_model(Models):
    def __init__(self,n,m):
        super().__init__(n,m)
        

    def __str__(self):
        return f"Data:{n} rows {m} columns."

    def learn_linear_regression(self,k, tau, lmbda,sigma):
        self.sigma=sigma
        self.k=k
        self.tau=tau
        self.lmbda=lmbda
        self.X_new,self.y=self.linear_regreion(self.sigma)
        self.beta=np.random.randn(self.m+1,1)
        self.prev_cost=float('inf')
        for i in range(self.k):
            self.y_pred=np.dot(self.X_new,self.beta)
            self.e=self.y_pred-self.y
            self.grad=np.dot(self.X_new.T,self.e)/self.n
            self.beta=self.beta-self.lmbda*self.grad
            self.cost = (1 / (2 * self.n)) * np.sum((self.y_pred - self.y)**2)
            self.new_cost=self.prev_cost-self.cost
            self.prev_cost=self.cost
            if(abs(self.new_cost)<self.tau):
                break
        return self.beta,self.cost

    def logistic_parameter(self,k,tao,lemda,theta):
        self.theta=theta
        self.k=k
        self.tao=tao
        self.lemda=lemda
        self.X_new,self.Y=self.logistic_regression(theta)
        self.beta=np.random.randn(self.m+1,1)
        self.prev_cost=float('inf')
        for i in range(self.k):
            self.y_pred=1/(1+np.exp(-1*(self.X_new@self.beta)))
            self.e=self.y_pred-self.Y
            self.grad=self.X_new.T@self.e/self.n
            self.beta=self.beta-self.lemda*self.grad
            self.cost=(-1/self.n )*np.sum(self.Y*np.log(self.y_pred)+(1-self.Y)*np.log(1-self.y_pred)) 
            self.dif_cost=self.prev_cost-self.cost
            self.prev_cost=self.cost
            if(abs(self.dif_cost)<self.tao):
                break
        return self.beta,self.cost

if __name__ == "__main__":
    n=int(input("Enter the number of rows :"))
    m=int(input("Enter the number of column :"))
    model1=Learn_model(n,m)
    print("------------------\nlinear regression Model\n------------------")
    
    sigma=int(input("Enter the Value of sigma :"))
    X,Y=model1.linear_regreion(sigma)
    print("X [array of independent variable values] :\n",X,"\n")
    print("Y [array of dependent variable values] :\n",Y,"\n")

    print("Learning the parameters :\n")
    k=int(input("Enter the number of iterations :"))
    tao=float(input("Enter the value of tao :"))
    lemda=float(input("Enter the learing rate value :"))
    beta,cost=model1.learn_linear_regression(k,tao,lemda,sigma)
    print("Array of Parameter Values:\n",beta,"\n")
    print("Cost function value:",cost,"\n")

    model2=Learn_model(n,m)
    print("------------------\nlogistic regression Model\n------------------")
    
    theta=float(input("Enter the Value of theta:"))
    X,Y=model2.logistic_regression(theta)
    print("X [array of independent variable values] :\n",X,"\n")
    print("Y [array of dependent variable values] :\n",Y,"\n")

    print("Learning the parameters :\n")
    k=int(input("Enter the number of iterations :"))
    tao=float(input("Enter the value of tao :"))
    lemda=float(input("Enter the learing rate value :"))
    beta,cost=model2.logistic_parameter(k,tao,lemda,theta)
    print("Array of Parameter Values:\n",beta,"\n")
    print("Cost function value:",cost,"\n")
    
    


    

    
        
        
        