class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        s = []
        i,j = 0,0
        
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]==nums2[j]:
                s.append(nums1[i])
                i,j=i+1,j+1
                
            elif nums1[i]<nums2[j]:
                i+=1
                
            else: 
                j+=1
                
        return s