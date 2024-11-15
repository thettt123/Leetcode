class Solution:
    def maxDepth(self, s: str) -> int:
        c = m = 0
        
        for si in filter(lambda x: x in "()", s):
            c += 2 * (si == "(") - 1
            m = max(c, m)
            
        return m