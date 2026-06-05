class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            check_row = []
            check_column = []
            for j in range(len(board[0])):   
                if(board[i][j] != "."):                 
                    if(board[i][j] not in check_row):
                         check_row.append(board[i][j])
                    else:
                        return False

                if(board[j][i] != "."):       
                    if(board[j][i] not in check_column):
                        check_column.append(board[j][i])                 
                    else:
                        return False
        
        for rows in range(0, 9, 3):
            for cols in range(0, 9, 3):
                seen = []
                for z in range(rows, rows+3):
                    for x in range(cols, cols+3):
                        if(board[z][x] != "."):
                            if(board[z][x] not in seen):
                                seen.append(board[z][x])
                            else:
                                return False
                print(seen)
        return True       
        