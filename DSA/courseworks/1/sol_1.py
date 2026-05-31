def longest_subarray_with_sum_k(arr, k):
    prefix_sum_map = {}
    current_sum = 0
    max_len = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum == k:
            max_len = i + 1
            
        if (current_sum - k) in prefix_sum_map:
            max_len = max(max_len, i - prefix_sum_map[current_sum - k])
            
        if current_sum not in prefix_sum_map:
            prefix_sum_map[current_sum] = i
            
    return max_len

arr = [10, 5, 2, 7, 1, -10]
k = 15
print(longest_subarray_with_sum_k(arr, k))