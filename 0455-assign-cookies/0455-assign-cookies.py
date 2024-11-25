class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g and not s:
            return 0

        answer = l = 0
        g.sort()
        s.sort()

        for child in g:
            for i in range(l, len(s)):
                if child <= s[i]:
                    answer += 1  
                    l = i
                    s.pop(i)
                    break
            
            else:
                return answer
        
        return answer