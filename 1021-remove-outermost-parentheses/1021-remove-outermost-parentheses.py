class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        result = []
        balance = 0
        
        for char in s:
            if char == '(':
                if balance > 0:  # Only add if we're not at the outermost '('
                    result.append(char)
                balance += 1
            else:  # char == ')'
                if balance > 1:  # Only add if we're not at the outermost ')'
                    result.append(char)
                balance -= 1
        
        return ''.join(result)
