class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        matrix = [["" for _ in range(3)] for _ in range(3)]
        move = 0
        
        for r, c in moves:
            matrix[r][c] = "A" if move % 2 == 0 else "B"
            move += 1
        
        for i in range(3):
            if matrix[i][0] == matrix[i][1] and matrix[i][1] == matrix[i][2] and matrix[i][0] != "": return matrix[i][0]
            if matrix[0][i] == matrix[1][i] and matrix[1][i] == matrix[2][i] and matrix[0][i] != "": return matrix[0][i]
            
        if (matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] and matrix[0][0] != "") or (matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0] and matrix[0][2] != ""):
            return matrix[1][1]
            
        if len(moves) == 9:
            return "Draw"
        
        else:
            return "Pending"