class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        co=Counter(nums)
        c=0
        
        for i in co.values():
            c+=(i*(i-1))//2
            
        return c