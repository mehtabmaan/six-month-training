def findSmallestMissing(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # If the value matches the index, the missing element is to the right
        if nums[mid] == mid:
            left = mid + 1
        else:
            # The missing element is at mid or to the left
            right = mid - 1
            
    # The 'left' pointer will eventually land on the smallest missing element
    return left

# Test Cases
print(findSmallestMissing([0, 1, 2, 6, 9, 11, 15]))  # Output: 3
print(findSmallestMissing([1, 2, 3, 4, 6, 9, 11, 15]))  # Output: 0