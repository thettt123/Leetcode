class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dic = {}
        lst = []
        k = s1 + " " + s2
        k2 = k.split()

        for j in k2:
            if j in dic:
                dic[j] += 1
                
            else:
                dic[j] = 1
        
        for x, y in dic.items():
            if y == 1:
                lst.append(x)
        
        return lst