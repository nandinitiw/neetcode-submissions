class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCond = False
        colCond = False
        boxCond = False
        #need to check for no duplicates

        #basics
        if(len(board)!=9):
            return False
        for i in range(9):
            if(len(board[i])!=9):
                return False

        #rows
        for i in range(9):
            numset = set()
            for k in range(1,10):
                numset.add(str(k))
            #print(numset)

            for j in range(9):
                if board[i][j] in numset:
                    numset.remove(board[i][j]);
                elif board[i][j] != ".":
                    return False

        rowCond = True

        #columns
        for i in range(9):
            numset = set()
            for k in range(1,10):
                numset.add(str(k))

            for j in range(9):
                if board[j][i] in numset:
                    numset.remove(board[j][i]);
                elif board[j][i] != ".":
                    return False

        colCond = True

        #boxes
        for square in range(9):
            numset = set()
            for k in range(1,10):
                numset.add(str(k))
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] in numset:
                        numset.remove(board[row][col]);
                    elif board[row][col] != ".":
                        return False


        boxCond = True


        return(rowCond and colCond and boxCond)

        