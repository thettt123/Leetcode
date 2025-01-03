class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        
        for i in range(0, len(points) - 1):
            x_dist = abs(points[i+1][0] - points[i][0])
            y_dist = abs(points[i+1][1] - points[i][1])
            total += max(x_dist, y_dist)
            
        return total        