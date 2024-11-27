class Solution:
	def largestPerimeter(self, nums: List[int]) -> int:
		nums = sorted(nums)
		i = len(nums)-3

		while i>-1:
			if nums[i]+nums[i+1] > nums[i+2]:
				return nums[i]+nums[i+1]+nums[i+2]
			i = i - 1

		return 0