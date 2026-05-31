import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def run_regression_simulation():
    # Define the true coefficients we want the model to learn
    true_beta = np.array([4.5, -2.1, 7.3])
    num_features = len(true_beta)
    
    # Define the parameters to test
    n_values = [20, 50, 100, 500, 1000, 5000]
    sigma_values = [0.1, 1.0, 5.0, 10.0]
    
    # Dictionary to store the coefficient errors
    results = {sigma: [] for sigma in sigma_values}
    
    # Run simulation
    np.random.seed(42) # For reproducibility
    
    for sigma in sigma_values:
        for n in n_values:
            # 1. Generate random feature matrix X
            X = np.random.randn(n, num_features)
            
            # 2. Generate noise epsilon
            noise = np.random.normal(0, sigma, size=n)
            
            # 3. Generate target vector y = X*beta + noise
            y = np.dot(X, true_beta) + noise
            
            # 4. Fit the linear regression model
            model = LinearRegression(fit_intercept=False)
            model.fit(X, y)
            learned_beta = model.coef_
            
            # 5. Calculate how far off the learned coefficients are from the true coefficients
            # Using Mean Squared Error of the coefficients: ||beta_hat - beta||^2
            coef_error = mean_squared_error(true_beta, learned_beta)
            results[sigma].append(coef_error)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    
    for sigma in sigma_values:
        plt.plot(n_values, results[sigma], marker='o', label=f'Noise $\sigma$ = {sigma}')
        
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Sample Size (n) - Log Scale')
    plt.ylabel('Coefficient Error (MSE of $\hat{\\beta}$) - Log Scale')
    plt.title('Impact of $n$ and $\sigma$ on Learning True Coefficients $\\beta$')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()

if __name__ == "__main__":
    run_regression_simulation()