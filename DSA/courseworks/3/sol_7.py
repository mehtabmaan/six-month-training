def countConsistentStrings(allowed, words):
    # Convert allowed characters to a set for O(1) lookups
    allowed_set = set(allowed)
    consistent_count = 0
    
    for word in words:
        is_consistent = True
        for char in word:
            if char not in allowed_set:
                is_consistent = False
                break
        
        if is_consistent:
            consistent_count += 1
            
    return consistent_count