class Solution:
    def removePalindromeSub(self, s: str) -> int:
        tjr = s[::-1]
        print(tjr)
        
        if s == tjr:
            return 1
        else:
            return 2
        