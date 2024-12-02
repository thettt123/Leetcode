class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic, count = defaultdict(int), 0

        for i, j in dominoes:
            mini = min(i, j)
            maxi = max(i, j)
            count += dic[(mini, maxi)]
            dic[(mini, maxi)] += 1 

        return count