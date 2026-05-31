def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    # Start at the top-right corner
    rows = len(matrix)
    cols = len(matrix[0])
    row = 0
    col = cols - 1
    
    while row < rows and col >= 0:
        current = matrix[row][col]
        
        if current == target:
            return True
        elif current > target:
            # Move left: current is too big, and everything below it is bigger
            col -= 1
        else:
            # Move down: current is too small, and everything to the left is smaller
            row += 1
            
    return False