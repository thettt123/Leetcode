class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        a={keysPressed[0]:releaseTimes[0]}
        
        for i in range(1,len(keysPressed)):
            if keysPressed[i] in a:
                print(keysPressed[i],a[keysPressed[i]])
                a[keysPressed[i]]=max(a[keysPressed[i]],abs(releaseTimes[i]-releaseTimes[i-1]))
            else:
                a[keysPressed[i]]=abs(releaseTimes[i]-releaseTimes[i-1])
                
        v=max(a,key=lambda k:(a[k],k))
        
        return v