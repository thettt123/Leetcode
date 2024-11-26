class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        x = max(cnt.values())
        frequent = [i for i in cnt if cnt[i]==x]
        minLength = len(nums)
        
        if x==1:
            return 1
        
        for i in frequent:
            upperIndex = len(nums) - 1 - nums[::-1].index(i)
            lowerIndex = nums.index(i)
            minLength = min(upperIndex-lowerIndex+1, minLength)
            
        return minLength