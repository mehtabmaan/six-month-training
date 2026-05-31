def removeDuplicates(s: str) -> str:
    stack = []
    
    for char in s:
        # If the stack has elements and the top matches the current char
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    # Join the stack characters to form the final string
    return "".join(stack)