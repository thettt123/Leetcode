class Solution:
    def modifyString(self, s: str) -> str:
        s1=list(s)
        
        for i in range(len(s1)):
            if s1[i]=="?":
                for j in "abc":
                    if (i==0 or s1[i-1]!=j)and(i==len(s1)-1 or s1[i+1]!=j):
                        s1[i]=j
                        break
                        
        return "".join(s1)
    

        