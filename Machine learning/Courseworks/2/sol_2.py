import numpy as np
def logistic_parameter(X,Y,k,tao,lemda):
    n,m=X.shape
    ones=np.ones((n,1))
    X_new=np.hstack((ones,X))
    beta=np.random.randn(m+1,1)
    prev_cost=float('inf')
    for i in range(k):
        y_pred=1/(1+np.exp(-1*(X_new@beta)))
        e=y_pred-Y
        grad=X_new.T@e/n
        beta=beta-lemda*grad
        cost=(-1/n )*np.sum(Y*np.log(y_pred)+(1-Y)*np.log(1-y_pred)) 
        dif_cost=prev_cost-cost
        prev_cost=cost
        if(abs(dif_cost)<tao):
            break
    return beta,cost
        
    
        
        
    
        
        