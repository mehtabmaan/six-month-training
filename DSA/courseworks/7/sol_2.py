class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Check if this is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Count upwards as long as consecutive numbers exist in the set
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the maximum length found
                longest_streak = max(longest_streak, current_streak)

        return longest_streak