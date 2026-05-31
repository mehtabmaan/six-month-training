"""
Task 3: Investigation of Logistic Regression Parameters
------------------------------------------------------
This script investigates how sample size (n) and the labeling threshold (theta) 
impact the model's ability to recover the true coefficients (beta).

PART 1: DERIVATION OF THE PARTIAL DERIVATIVE
The cost function (Log-Loss) for Logistic Regression is:
    J(β) = -(1/n) * Σ [y_i * log(h(x_i)) + (1 - y_i) * log(1 - h(x_i))]
    where h(x) = σ(xβ) = 1 / (1 + e^(-xβ))

To find ∂J/∂β_j:
1. Note that the derivative of the sigmoid σ(z) is σ(z)(1 - σ(z)).
2. Using the chain rule: ∂J/∂β_j = (∂J/∂h) * (∂h/∂z) * (∂z/∂β_j)
3. ∂J/∂h = -(y/h) + (1-y)/(1-h) = (h - y) / [h(1 - h)]
4. ∂h/∂z = h(1 - h)
5. ∂z/∂β_j = x_j
6. Multiplying these: [(h - y) / (h(1 - h))] * [h(1 - h)] * x_j = (h - y)x_j

Result:
    ∂J/∂β_j = (1/n) * Σ (σ(x_i * β) - y_i) * x_{i,j}
"""

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_gradient(X, y, beta):
    n = len(y)
    predictions = sigmoid(X @ beta)
    gradient = (1/n) * (X.T @ (predictions - y))
    return gradient

def fit_logistic_regression(X, y, lr=0.1, iterations=1000):
    beta = np.zeros(X.shape[1])
    for _ in range(iterations):
        grad = compute_gradient(X, y, beta)
        beta -= lr * grad
    return beta

# --- INVESTIGATION ---

def run_investigation():
    # Set true beta
    true_beta = np.array([1.5, -2.0])
    
    # 1. Impact of n (Sample Size)
    n_values = [10, 50, 100, 500, 1000, 5000]
    errors_n = []
    
    print("Investigating n (Sample Size)...")
    for n in n_values:
        X = np.random.randn(n, 2)
        # Generate probabilities
        probs = sigmoid(X @ true_beta)
        # Generate labels (using standard theta = 0.5)
        y = (probs >= 0.5).astype(int)
        
        learned_beta = fit_logistic_regression(X, y)
        error = np.linalg.norm(true_beta - learned_beta)
        errors_n.append(error)
        print(f"n={n:4d} | Beta Error: {error:.4f}")

    # 2. Impact of theta (Threshold used to generate Y)
    # Note: Theta is often a decision boundary, but if we use it to 
    # generate Y from probabilities, it changes the bias of the data.
    theta_values = [0.1, 0.3, 0.5, 0.7, 0.9]
    errors_theta = []
    n_fixed = 1000
    
    print("\nInvestigating theta (Labeling Threshold)...")
    for theta in theta_values:
        X = np.random.randn(n_fixed, 2)
        probs = sigmoid(X @ true_beta)
        # Thresholding the continuous probability to create binary Y
        y = (probs >= theta).astype(int)
        
        learned_beta = fit_logistic_regression(X, y)
        error = np.linalg.norm(true_beta - learned_beta)
        errors_theta.append(error)
        print(f"theta={theta:.1f} | Beta Error: {error:.4f}")

    # Visualizing results
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax1.plot(n_values, errors_n, marker='o', color='b')
    ax1.set_title('Impact of Sample Size (n) on Beta Recovery')
    ax1.set_xlabel('n (Number of samples)')
    ax1.set_ylabel('L2 Norm Error of Beta')
    ax1.grid(True)

    ax2.plot(theta_values, errors_theta, marker='s', color='r')
    ax2.set_title('Impact of Threshold (theta) on Beta Recovery')
    ax2.set_xlabel('Theta (Classification Threshold)')
    ax2.set_ylabel('L2 Norm Error of Beta')
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_investigation()