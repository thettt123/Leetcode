class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr) 
        if s % 3 != 0:
            return False 
        
        each = s // 3
        n = len(arr)     
        cnt = 0
        frq = 0
        
        for i in range(n):
            cnt += arr[i]
            if cnt == each:
                cnt = 0
                frq += 1
            if frq == 3:
                return True
            
        return False