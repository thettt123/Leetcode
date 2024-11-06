class Solution:
    def toLowerCase(self, s: str) -> str:

        res = ''

        for char in s:
            if char.isupper():
                res += char.lower()
            else:
                res += char
        
        return res