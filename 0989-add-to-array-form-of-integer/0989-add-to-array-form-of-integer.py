class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans=[]
        n=len(num)
        
        while n>0 or k!=0:
            if n>0:
                n -=1
                k+=num[n]
                
            ans.append(k%10)
            k=k//10
            
        newlis=ans[::-1]
        
        return newlis