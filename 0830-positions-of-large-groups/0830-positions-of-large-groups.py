class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        start = 0
        
        while start < len(s):
            end = start
            
            while end < len(s) and s[end] == s[start]:
                end += 1
            if end - start >= 3:
                ans.append([start, end - 1])
            
            start = end
        
        return ans
