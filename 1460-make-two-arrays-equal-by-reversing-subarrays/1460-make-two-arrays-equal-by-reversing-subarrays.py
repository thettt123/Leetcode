class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr.sort()
        target.sort()
        
        return  arr ==target