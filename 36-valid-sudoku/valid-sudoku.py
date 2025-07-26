class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {}
        col_map = {}
        box_map = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num == ".":
                    continue

                if ( (i,num) in row_map ) or ( (j,num) in col_map ) or ( (i//3,j//3, num) in box_map ):
                    return False
                
                row_map[( i, num )] = 1
                col_map[( j, num )] = 1
                box_map[( i//3, j//3, num )] = 1
        
        return True

        
