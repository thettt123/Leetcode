class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()  # Remove the last character since it's a duplicate
                
            else:
                stack.append(char)  # Add the current character to the stack
        
        return ''.join(stack)  # Join the characters in the stack to form the final string

 