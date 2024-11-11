class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a = []
        answer = []
        for i in range(len(s)):
            if s[i] == c:
                a.append(i)
                
        for i in range(len(s)):
            t = []
            for j in a:
                t.append(abs(i-j))
            answer.append(min(t))
        
        return answer