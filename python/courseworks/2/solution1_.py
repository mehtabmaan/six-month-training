def threeSum(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        seen = set()
        target = -nums[i]

        for j in range(i + 1, n):
            
            complement = target - nums[j]

            if complement in seen:
                result.append([nums[i], complement, nums[j]])
                
                # Skip duplicates for second number
                while j + 1 < n and nums[j] == nums[j + 1]:
                    j += 1
            
            seen.add(nums[j])

    return result


# Test cases
lis1 = [-1,0,1,2,-1,-4]
print(threeSum(lis1))

lis2 = [0,1,1]
print(threeSum(lis2))

lis3 = [0,0,0]
print(threeSum(lis3))