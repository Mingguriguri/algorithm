# pypy3로 통과

import sys
input = sys.stdin.readline

# 유망한지 판단하는 함수
def isPromissing(board, new):
        for i in range(new):

            # 같은 열이면 안 되고, 대각선상에 있어서도 안 된다.
            if board[new] == board[i] or new - i == abs(board[new]-board[i]):
                return 0
        return 1
    
# N Queen 알고리즘 수행
def nQueen(new, board):
    global n
    global count
    print(board)
    # n 이 마지막행까지 수행하고 여기까지 오면 찾기 완료!
    if new == n:
        count += 1
        return
    for i in range(n):
        board[new] = i
        if isPromissing(board, new):
            nQueen(new + 1, board)

count = 0
board = [0] * 15
n = int(input())
nQueen(0, board)
print(count)