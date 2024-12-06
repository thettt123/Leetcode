class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        num1 = -1
        n = len(arr)
        
        for i in range(n-1,-1,-1):
            arr[i],temp = num1,arr[i]
            num1 = max(num1,temp)
        
        return arr