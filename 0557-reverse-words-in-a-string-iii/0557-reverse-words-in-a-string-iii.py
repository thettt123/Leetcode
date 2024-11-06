class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split(" ")
        ans=""
        n=len(lst)
        
        for i in range(n):
            ans+=lst[i][::-1]
            
            if i==n-1:
                return ans
            
            ans+=" "
        
        