
def printBoard(board, N):
    for i in range(N):
        for j in range(N):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()
    print()



def isSafe(board, row, col, N):
    
    
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True



def solveNQueens(board, row, N):
    
    
    if row == N:
        return True
    
    
    for col in range(N):
        
        
        if isSafe(board, row, col, N):
            
            board[row][col] = 1  
            
            
            if solveNQueens(board, row + 1, N):
                return True
            
            board[row][col] = 0  
    
    return False



N = 4  


board = [[0 for _ in range(N)] for _ in range(N)]

if solveNQueens(board, 0, N):
    print("Solution:")
    printBoard(board, N)
else:
    print("No solution exists")