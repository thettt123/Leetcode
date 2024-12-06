class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        a = 0
        
        arr.sort()
        target.sort()
        
        return  arr ==target