import numpy as np

# --- 1: Numpy array creation and manipulation ---

def create_1d_array_a():
    return np.random.randint(0, 100, size=10)

def create_2d_array_b():
    """1.2 Create a 2D Numpy array 'b' of shape (3, 4) with random integers [-10, 10]."""
    return np.random.randint(-10, 11, size=(3, 4))

def flatten_array_b(b):
    """1.3 Flatten the array 'b' into a 1D NumPy array named 'b_flat'."""
    return b.flatten()

def modify_copy_of_a(a):
    """1.4 Create a copy 'a_copy' and set the first element to -1."""
    a_copy = a.copy()
    a_copy[0] = -1
    return a_copy

def slice_every_second_element(a):
    """1.5 Create a 1D Numpy array 'c' containing every second element of 'a'."""
    return a[::2]

# --- 2: Numpy array indexing and slicing ---

def get_third_element(a):
    """2.1 Print the third element of 'a'."""
    return a[2]

def get_last_element_2d(b):
    """2.2 Print the last element of 'b' (bottom-right)."""
    return b[-1, -1]

def get_sub_matrix(b):
    """2.3 Print the first two rows and last two columns of 'b'."""
    return b[:2, -2:]

def get_second_row(b):
    """2.4 Assign the second row of 'b' to 'b_row'."""
    return b[1, :]

def get_first_column(b):
    """2.5 Assign the first column of 'b' to 'b_col'."""
    return b[:, 0]

# --- 3: Numpy array operations ---

def create_range_array_d():
    """3.1 Create a 1D Numpy array 'd' containing integers from 1 to 10."""
    return np.arange(1, 11)

def add_arrays_a_d(a, d):
    """3.2 Add 'a' and 'd' element-wise to create 'e'."""
    return a + d

def multiply_b_by_2(b):
    """3.3 Multiply 'b' by 2 to create 'b_double'."""
    return b * 2

def matrix_multiply_b_transpose(b, b_double):
    """3.4 Calculate matrix multiplication of 'b' and transpose of 'b_double'."""
    return np.matmul(b, b_double.T)

def calculate_means(a, b, b_double):
    """3.5 Calculate mean of a, b, and b_double and store in array 'g'."""
    return np.array([np.mean(a), np.mean(b), np.mean(b_double)])

# --- 4: Numpy array aggregation ---

def sum_array_a(a):
    """4.1 Find the sum of every element in 'a'."""
    return np.sum(a)

def min_array_b(b):
    """4.2 Find the minimum element in 'b'."""
    return np.min(b)

def max_array_b_double(b_double):
    """4.3 Find the maximum element in 'b_double'."""
    return np.max(b_double)


if __name__ == "__main__":
    # Task Group 1
    a = create_1d_array_a()
    b = create_2d_array_b()
    b_flat = flatten_array_b(b)
    a_copy = modify_copy_of_a(a)
    c = slice_every_second_element(a)
    
    print("--- 1: Creation & Manipulation ---")
    print(f"Array a: {a}")
    print(f"Array b:\n{b}")
    print(f"b_flat: {b_flat}")
    print(f"a_copy (first element modified): {a_copy}")
    print(f"Array c (every second of a): {c}\n")

    # Task Group 2
    print("--- 2: Indexing & Slicing ---")
    print(f"Third element of a: {get_third_element(a)}")
    print(f"Bottom-right of b: {get_last_element_2d(b)}")
    print(f"First 2 rows, last 2 cols of b:\n{get_sub_matrix(b)}")
    b_row = get_second_row(b)
    b_col = get_first_column(b)
    print(f"b_row (2nd row): {b_row}")
    print(f"b_col (1st col): {b_col}\n")

    # Task Group 3
    d = create_range_array_d()
    e = add_arrays_a_d(a, d)
    b_double = multiply_b_by_2(b)
    f = matrix_multiply_b_transpose(b, b_double)
    g = calculate_means(a, b, b_double)
    
    print("--- 3: Operations ---")
    print(f"Array d: {d}")
    print(f"Array e (a + d): {e}")
    print(f"Array b_double:\n{b_double}")
    print(f"Matrix f (b @ b_double.T):\n{f}")
    print(f"Array g (Means of a, b, b_double): {g}\n")

    # Task Group 4
    a_sum = sum_array_a(a)
    b_min = min_array_b(b)
    b_double_max = max_array_b_double(b_double)
    
    print("--- 4: Aggregation ---")
    print(f"Sum of a: {a_sum}")
    print(f"Min of b: {b_min}")
    print(f"Max of b_double: {b_double_max}")