class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = list(range(n+1))
        
        for i in s:
            if i not in nums:
                return i