def chocolate(arr, m):
    
    n = len(arr)

    if m > n:
        return 0

    arr.sort()
    
    min_diff = float('inf')

    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]

        if diff < min_diff:
            min_diff = diff

    return min_diff


arr1 = [7, 3, 2, 4, 9, 12, 56]
print(chocolate(arr1, 3))

arr2 = [3, 4, 1, 9, 56, 7, 9, 12]
print(chocolate(arr2, 5))