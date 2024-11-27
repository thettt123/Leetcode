class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        
        for i in image:
            i.reverse()
            ans.append([x ^ 1 for x in i])
            
        return ans