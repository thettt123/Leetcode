class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        r = len(grid)
        c = len(grid[0])
        total = r * c
        k = k % total
        
        full_list = [grid[i][j] for i in range(r) for j in range(c)]
        full_list = full_list[-k:] + full_list[:-k]
        
        return [full_list[i * c:(i + 1) * c] for i in range(r)]