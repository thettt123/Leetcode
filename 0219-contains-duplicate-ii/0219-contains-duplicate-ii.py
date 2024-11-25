class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        s = {}

        for i in range(n):
            if nums[i] in s and i - s[nums[i]] <= k:
                return True
            
            s[nums[i]] = i
        
        return False
