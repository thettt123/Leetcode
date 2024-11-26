class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        a = nums[0]
        cnt = 1
        ans = 1
        
        for num in nums[1:]:
            if num > a:
                cnt += 1
            else:
                cnt = 1
            a = num
            ans = max(ans, cnt)
        return ans