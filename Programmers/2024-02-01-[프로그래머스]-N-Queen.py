def solution(n):
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
    return nQueen(n, [])