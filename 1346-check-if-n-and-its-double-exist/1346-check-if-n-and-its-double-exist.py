class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        sort_arr = sorted(arr)
        size = len(sort_arr)

        for x in range(size):
            if sort_arr[x] >= 0:
                if sort_arr[x] * 2 in sort_arr[x+1:]:
                    return True
            else:              
                if sort_arr[x] * 2 in sort_arr[:x]:
                    return True
                
        return False
        