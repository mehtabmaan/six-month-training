import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the dataset
def load_dataset(file_path):
    """Loads the dataset and returns the first 5 rows."""
    df = pd.read_csv(file_path)
    return df

# 2. Clean the dataset
def clean_dataset(df):
    """Removes duplicates/missing values and converts text-based numeric columns to floats."""
    # Remove missing and duplicate values
    df = df.dropna().drop_duplicates()

    # Helper function to clean numeric strings (remove commas, $, etc.)
    def clean_currency_string(value):
        if isinstance(value, str):
            # Remove characters that prevent numeric conversion
            value = value.replace(',', '').replace('$', '').replace('+', '').strip()
        try:
            return float(value)
        except ValueError:
            return np.nan

    # Apply cleaning to relvant columns
    # Adjust column names based on the actual CSV structure (e.g., 'Price (in USD)')
    target_columns = ['Price (in USD)', 'Horsepower', '0-60 MPH Time (seconds)']
    for col in target_columns:
        if col in df.columns:
            df[col] = df[col].apply(clean_currency_string)

    # Final drop of any rows that failed conversion
    return df.dropna()

# 3. Explore dataset statistics
def compute_summary_statistics(df):
    """Computes mean, median, mode, std dev, and range for numeric columns."""
    stats = df.describe().transpose()
    # Calculate Range: max - min
    stats['range'] = stats['max'] - stats['min']
    # Calculate Median separately as it's not in standard describe()
    stats['median'] = df.median(numeric_only=True)
    # Mode can return multiple values, we take the first
    stats['mode'] = df.mode(numeric_only=True).iloc[0]
    
    return stats[['mean', 'median', 'mode', 'std', 'range']]

# 4. Average price by make
def average_price_by_make(df):
    """Groups by car make and computes average price."""
    return df.groupby('Car Make')['Price (in USD)'].mean()

# 5. Average horsepower by year
def average_horsepower_by_year(df):
    """Groups by year and computes average horsepower."""
    return df.groupby('Year')['Horsepower'].mean()

# 6. Scatter plot with regression line
def plot_price_vs_horsepower(df):
    """Creates a scatter plot with a linear regression line."""
    x = df['Horsepower']
    y = df['Price (in USD)']
    
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.5, label='Data Points')
    
    # Calculate regression line
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b, color='red', label=f'Regression Line (y={m:.2f}x + {b:.2f})')
    
    plt.title('Price vs Horsepower')
    plt.xlabel('Horsepower')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()
    return (m, b)

# 7. Histogram of 0-60 MPH times
def plot_acceleration_histogram(df):
    """Creates a histogram for 0-60 MPH times with bins of 0.5s."""
    times = df['0-60 MPH Time (seconds)']
    bins = np.arange(min(times), max(times) + 0.5, 0.5)
    
    plt.figure(figsize=(10, 6))
    plt.hist(times, bins=bins, edgecolor='black', color='skyblue')
    plt.title('Distribution of 0-60 MPH Times')
    plt.xlabel('Seconds')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()
    return bins

# 8. Filter and sort
def filter_and_sort_cars(df):
    """Filters cars > $500,000 and sorts by Horsepower descending."""
    filtered_df = df[df['Price (in USD)'] > 500000]
    return filtered_df.sort_values(by='Horsepower', ascending=False)

# 9. Export to CSV
def export_dataset(df, filename):
    """Exports the cleaned dataframe to a CSV file."""
    df.to_csv(filename, index=False)
    return f"File saved as {filename}"

if __name__ == "__main__":
    # Path to the downloaded Kaggle file
    file_path = "Sport car price.csv" 
    
    try:
        # Task 1
        raw_data = load_dataset(file_path)
        print("--- Task 1: First 5 Rows ---")
        print(raw_data.head(), "\n")

        # Task 2
        cleaned_data = clean_dataset(raw_data)
        print("--- Task 2: Data Cleaned ---\n")

        # Task 3
        print("--- Task 3: Summary Statistics ---")
        print(compute_summary_statistics(cleaned_data), "\n")

        # Task 4
        print("--- Task 4: Avg Price by Make (Top 5) ---")
        print(average_price_by_make(cleaned_data).sort_values(ascending=False).head(), "\n")

        # Task 5
        print("--- Task 5: Avg Horsepower by Year ---")
        print(average_horsepower_by_year(cleaned_data), "\n")

        # Task 6 & 7 (Displays plots)
        plot_price_vs_horsepower(cleaned_data)
        plot_acceleration_histogram(cleaned_data)

        # Task 8
        print("--- Task 8: Cars > $500k Sorted by Horsepower ---")
        print(filter_and_sort_cars(cleaned_data).head(), "\n")

        # Task 9
        status = export_dataset(cleaned_data, "Cleaned_Sports_Cars.csv")
        print(f"--- Task 9: {status} ---")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please ensure it is in the same directory.")