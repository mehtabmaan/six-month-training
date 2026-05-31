def can_jump(nums):
    max_reach = 0
    target = len(nums) - 1
    
    for i, jump in enumerate(nums):
        # If the current index is further than we can ever reach, fail
        if i > max_reach:
            return False
        
        # Update the furthest index we can reach from here
        max_reach = max(max_reach, i + jump)
        
        # Early exit: if we can already reach the end, no need to keep checking
        if max_reach >= target:
            return True
            
    return max_reach >= target

# --- User Input Handling ---
if __name__ == "__main__":
    try:
        raw_input = input("Enter the integer array (space-separated): ")
        nums = [int(x) for x in raw_input.split()]
        
        if not nums:
            print("Array cannot be empty.")
        else:
            result = can_jump(nums)
            print(f"Can reach the last index: {result}")
            
    except ValueError:
        print("Invalid input. Please enter integers only.")