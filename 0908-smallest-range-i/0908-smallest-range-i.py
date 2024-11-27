class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        a = max(nums)
        b = min(nums)
        
        return max(0,(a-k)-(b+k))