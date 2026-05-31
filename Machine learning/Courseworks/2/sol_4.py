"""
Task 4: L1 and L2 Regularization in Logistic Regression
------------------------------------------------------
This script investigates how regularization impacts the learning of 
coefficients (beta) and the effect of the regularization constant (lambda).

PART 1: REGULARIZED COST FUNCTIONS
1. L2 Regularization (Ridge):
   J(β)_L2 = J(β) + (λ / 2n) * Σ(β_j^2)
   Gradient: ∂J/∂β_j = (1/n) * Σ(h(x_i) - y_i)x_{i,j} + (λ/n) * β_j

2. L1 Regularization (Lasso):
   J(β)_L1 = J(β) + (λ / n) * Σ|β_j|
   Gradient: ∂J/∂β_j = (1/n) * Σ(h(x_i) - y_i)x_{i,j} + (λ/n) * sign(β_j)
"""

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    # Clip for numerical stability
    z = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z))

def fit_regularized_logistic(X, y, penalty='l2', lmbda=0.1, lr=0.1, iterations=1000):
    n, p = X.shape
    beta = np.zeros(p)
    
    for _ in range(iterations):
        predictions = sigmoid(X @ beta)
        base_grad = (1/n) * (X.T @ (predictions - y))
        
        if penalty == 'l2':
            # Add L2 penalty: lambda * beta
            grad = base_grad + (lmbda/n) * beta
        elif penalty == 'l1':
            # Add L1 penalty: lambda * sign(beta)
            grad = base_grad + (lmbda/n) * np.sign(beta)
        else:
            grad = base_grad
            
        beta -= lr * grad
    return beta

# --- INVESTIGATION ---

def run_task_4():
    # Set true beta (last three features are noise/irrelevant)
    true_beta = np.array([2.0, -1.5, 0.0, 0.0, 0.0])
    n = 200
    p = 5
    X = np.random.randn(n, p)
    probs = sigmoid(X @ true_beta)
    y = (probs >= 0.5).astype(int)

    lambdas = [0, 0.1, 1, 10, 50, 100]
    l1_results = []
    l2_results = []

    print(f"{'Lambda':<10} | {'L1 Beta (sum)':<15} | {'L2 Beta (sum)':<15}")
    print("-" * 45)

    for l in lambdas:
        beta_l1 = fit_regularized_logistic(X, y, penalty='l1', lmbda=l)
        beta_l2 = fit_regularized_logistic(X, y, penalty='l2', lmbda=l)
        
        l1_results.append(beta_l1)
        l2_results.append(beta_l2)
        
        print(f"{l:<10} | {np.sum(np.abs(beta_l1)):<15.4f} | {np.sum(np.abs(beta_l2)):<15.4f}")

    # Visualization
    l1_results = np.array(l1_results)
    l2_results = np.array(l2_results)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    for i in range(p):
        ax1.plot(lambdas, l1_results[:, i], marker='o', label=f'Beta_{i}')
    ax1.set_title('Impact of Lambda (L1 - Lasso)')
    ax1.set_xlabel('Lambda (Regularization Strength)')
    ax1.set_ylabel('Coefficient Value')
    ax1.legend()
    ax1.grid(True)

    for i in range(p):
        ax2.plot(lambdas, l2_results[:, i], marker='s', label=f'Beta_{i}')
    ax2.set_title('Impact of Lambda (L2 - Ridge)')
    ax2.set_xlabel('Lambda (Regularization Strength)')
    ax2.set_ylabel('Coefficient Value')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_task_4()