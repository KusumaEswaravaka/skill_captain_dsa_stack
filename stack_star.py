def removeStars(s):
    stack = []
    
    for char in s:
        if char == '*':
            if stack:
                stack.pop()  # Remove the closest non-star character to the left
        else:
            stack.append(char)  # Add the character to the stack
    
    return ''.join(stack)

# Example usage
s = "abc*de*f*"
print(removeStars(s))  # Output: "abd"
