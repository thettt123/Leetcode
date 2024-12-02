class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
            
        dis1 = sum(distance[start:destination])
        dis2 = sum(distance[destination:]) + sum(distance[:start])
        
        return min(dis1, dis2)