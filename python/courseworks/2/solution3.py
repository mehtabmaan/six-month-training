def pair_sum(nums, k):
    nums.sort()
    left = 0
    right = len(nums) - 1
    count = 0

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == k:

            if nums[left] == nums[right]:
                n = right - left + 1
                count += (n * (n - 1)) // 2
                break

            left_count = 1
            while left + 1 < right and nums[left] == nums[left + 1]:
                left_count += 1
                left += 1

            right_count = 1
            while right - 1 > left and nums[right] == nums[right - 1]:
                right_count += 1
                right -= 1

            count += left_count * right_count
            left += 1
            right -= 1

        elif current_sum < k:
            left += 1
        else:
            right -= 1

    return count


arr1 = [1,5,7,-1]
print(pair_sum(arr1,6))

arr2 = [1,5,7,-1,5]
print(pair_sum(arr2,6))