def next_permutation(nums):
    n = len(nums)
    pivot = -1
    
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break
            
    if pivot == -1:
        nums.reverse()
        return
        
    for i in range(n - 1, pivot, -1):
        if nums[i] > nums[pivot]:
            nums[i], nums[pivot] = nums[pivot], nums[i]
            break
            
    left, right = pivot + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Examples
nums1 = [1, 2, 3]
next_permutation(nums1)
print(nums1)

nums2 = [3, 2, 1]
next_permutation(nums2)
print(nums2)

nums3 = [1, 1, 5]
next_permutation(nums3)
print(nums3)