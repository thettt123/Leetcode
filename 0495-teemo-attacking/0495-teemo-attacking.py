class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0:
            return 0

        num_attacks = len(timeSeries)                
        poisoned_time = 0
        
        for attack in range(num_attacks - 1):
            if timeSeries[attack] + duration <= timeSeries[attack + 1]:
                poisoned_time += duration
            else:
                poisoned_time += (timeSeries[attack + 1] - timeSeries[attack])

        return poisoned_time + duration
         