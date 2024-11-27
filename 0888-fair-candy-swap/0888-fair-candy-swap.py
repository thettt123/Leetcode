class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum1 = sum(aliceSizes)
        sum2 = sum(bobSizes)
        c = (sum1 - sum2)//2
        d = set(aliceSizes)
        
        for i in bobSizes:      
            if i + c in d:
                return [i+c,i]  