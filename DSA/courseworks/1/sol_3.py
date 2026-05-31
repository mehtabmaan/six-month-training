def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        left = i + 1
        right = n - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
                
    return result

nums1 = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums1))

nums2 = [0, 1, 1]
print(three_sum(nums2))

nums3 = [0, 0, 0]
print(three_sum(nums3))