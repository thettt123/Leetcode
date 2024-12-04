class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        
        for x in arr:
            d[x] = d.get(x, 0) + 1

        return len(d) == len(set(d.values()))
