class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dict_data = {}
        ans = 0
        
        for i in nums:
            if dict_data.get(i):
                existing = dict_data.get(i)
                dict_data[i]= existing+1
                
            else:
                dict_data[i]=1
        
        max_value = max(dict_data.values())
        for key, value in dict_data.items():
            if value == max_value:
                ans = key
                
        return ans   