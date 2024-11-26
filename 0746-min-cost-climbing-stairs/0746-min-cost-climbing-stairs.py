class Solution(object):
    def minCostClimbingStairs(self, cost):
        for i in range(2,len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        ans = min(cost[-2], cost[-1])
            
        return ans