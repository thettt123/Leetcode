class Solution:
    def reformatNumber(self, number: str) -> str:
        
        n = ''.join(i for i in number if i.isalnum())
        new = ""
        
        while(len(n)>4):
            new+=n[0:3] + "-"
            n = n[3:]
            
        if len(n) == 3:
            new+=n[0:3]
            
        else:
            new+=n[0:2]
            n = n[2:]
            if len(n) > 0:
                new +="-" +n
                
        return new

            