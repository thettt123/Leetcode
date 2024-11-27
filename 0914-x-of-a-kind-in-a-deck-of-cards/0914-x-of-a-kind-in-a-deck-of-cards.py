class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        import math
        f = defaultdict(int)
        
        for j in deck:
            f[j] += 1
        
        u = list(f.values())
        
        g = u[0]
        
        for j in range(1,len(u)):
            g = math.gcd(g,u[j])
            
        return g!=1
      
        