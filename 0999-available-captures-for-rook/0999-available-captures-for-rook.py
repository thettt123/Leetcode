class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        col1 = 0
        row1 = 0
        res = 0

        for col in range(8):
            for row in range(8):
                if board[col][row] == 'R':
                    col1, row1 = col,row
                    break
                
        
        for i in range(col1 - 1,-1,-1):
            if board[i][row1] == 'p':
                res += 1
                break
            elif board[i][row1] =='B':
                break
        for i in range(col1 + 1, 8):
            if board[i][row1] == 'p':
                res += 1
                break
            elif board[i][row1] == 'B':
                break
        for j in range(row1 - 1,-1,-1):
            if board[col1][j] == 'p':
                res += 1
                break
            elif board[col1][j] == 'B':
                break
        for j in range(row1 + 1, 8):
            if board[col1][j] == 'p':
                res += 1
                break
            elif board[col1][j] =='B':
                break
        return res