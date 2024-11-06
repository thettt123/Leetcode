class Solution:
    def checkRecord(self, s: str) -> bool:
       
        count_A, count_L = 0, 0
        
        for c in s:
            if c == 'A':
                count_A += 1
                count_L = 0
            elif c == 'L':
                count_L += 1
            else:
                count_L = 0
            
            if count_A >= 2 or count_L >= 3:
                return False
        
        return True