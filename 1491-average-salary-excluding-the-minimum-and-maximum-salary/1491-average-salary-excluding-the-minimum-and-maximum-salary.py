class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        ans = []
        
        for i in range(1,len(salary)-1):
            ans.append(salary[i])
            
        return sum(ans)/len(ans)