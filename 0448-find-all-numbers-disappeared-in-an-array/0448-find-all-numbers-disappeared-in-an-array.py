
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = []
        set_nums = set(nums)

        for i in range(1,len(nums)+1):
            if i not in set_nums:
                s.append(i)

        return s