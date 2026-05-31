class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        sub = []
        
        for num in nums:
            # --- Manual Binary Search (Equivalent to bisect_left) ---
            left, right = 0, len(sub) - 1
            
            while left <= right:
                mid = left + (right - left) // 2  # Find the middle index
                
                if sub[mid] < num:
                    # Target is larger, search the right half
                    left = mid + 1
                else:
                    # Target is smaller or equal, search the left half
                    right = mid - 1
            # --------------------------------------------------------
            
            # 'left' is now the correct insertion index
            if left == len(sub):
                # The number is greater than all elements, extend the sequence
                sub.append(num)
            else:
                # Replace the element to keep the potential tails small
                sub[left] = num
                
        return len(sub)