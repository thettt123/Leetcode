class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s1 = sum(nums)
        s2 = 0
        
        for i in range(len(nums)):
            s2 += nums[i]
            if s2 == s1:
                return i
            s1 -= nums[i]
            
        return -1