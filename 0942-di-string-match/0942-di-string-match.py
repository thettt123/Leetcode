class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans=[0]*(len(s)+1)
        cnt=0
        h=len(s)
        
        for i in range(len(s)):
            if s[i]=="I":
                ans[i]=cnt
                cnt+=1
                
            else:
                ans[i]=h
                h-=1
                
        ans[-1]=cnt
        
        return ans