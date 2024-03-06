import sys
input = sys.stdin.readline

def backtracking(n, board):
    global cnt
    print(board)
    if len(board) == n:
        return

    for i in range(len(board)):
        for j in range(len(board)):
            if j == board[i] or abs(j - i) == abs(i - j):
                break
            board.append[j]
        cnt += backtracking(n, board + [i])
def isPromissing(board, new):
        for i in range(len(board)):
            if new == board[i] or len(board)-i == abs(board[i]-new):
                return False
        return True
    
def nQueen(n, board):
    if len(board) == n:
        return 1
    cnt = 0
    for i in range(n):
        if isPromissing(board, i):
            cnt += nQueen(n, board+[i])
            
    return cnt
cnt = 0
n = int(input())
#backtracking(n, [])
print(nQueen(n, []))