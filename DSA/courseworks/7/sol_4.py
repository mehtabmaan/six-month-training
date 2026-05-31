def hasOnlyOneChild(pre: list[int]) -> bool:
    # A tree with 2 or fewer nodes always has at most one child per internal node
    if len(pre) <= 2:
        return True
        
    # Initialize min and max with the last element (the single leaf node)
    min_val = pre[-1]
    max_val = pre[-1]
    
    # Traverse from the second-to-last element down to the first
    for i in range(len(pre) - 2, -1, -1):
        current = pre[i]
        
        # If the current node is strictly between the min and max of its descendants,
        # it must have both a left and right subtree (two children).
        if current > min_val and current < max_val:
            return False
            
        # Update the running min and max
        min_val = min(min_val, current)
        max_val = max(max_val, current)
        
    return True

# Test Cases
print(hasOnlyOneChild([20, 10, 11, 13, 12]))  # Output: True (Yes)
print(hasOnlyOneChild([15, 30, 25, 18, 20]))  # Output: True (Yes)
print(hasOnlyOneChild([20, 10, 25]))          # Output: False (No)