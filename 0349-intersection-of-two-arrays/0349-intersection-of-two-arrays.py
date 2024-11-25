class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = set(nums1)
        s = set()
        
        for num in nums2:
            if num in num1:
                s.add(num)
                
        return list(s)

        