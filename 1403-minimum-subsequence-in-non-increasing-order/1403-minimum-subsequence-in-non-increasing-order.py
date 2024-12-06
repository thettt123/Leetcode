class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        a = 0
        b = 0
        nums.sort(reverse=True)
        
        for i in range(len(nums)):
            a = sum(nums[0:i+1])
            b = sum(nums[i:len(nums)])-nums[i]
            
            if a>b:
                return nums[0:i+1]

