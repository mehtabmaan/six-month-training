def find_max_product_triplet(arr):
    if len(arr) < 3:
        return 0

    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

    for x in arr:
        if x > max1:
            max3 = max2
            max2 = max1
            max1 = x
        elif x > max2:
            max3 = max2
            max2 = x
        elif x > max3:
            max3 = x

        if x < min1:
            min2 = min1
            min1 = x
        elif x < min2:
            min2 = x

    prod1 = max1 * max2 * max3
    prod2 = min1 * min2 * max1

    if prod1 > prod2:
        return (max1, max2, max3)
    else:
        
        return (min1, min2, max1)

# Test Case 1
arr1 = [-4, 1, -8, 9, 6]
print(f"Input: {arr1} -> Output: {find_max_product_triplet(arr1)}")

# Test Case 2
arr2 = [1, 7, 2, -2, 5]
print(f"Input: {arr2} -> Output: {find_max_product_triplet(arr2)}")