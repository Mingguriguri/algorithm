import sys
input = sys.stdin.readline

def pattern(startX, startY, N):
    if N == 1: # N을 더이상 나눌 수 없을 때 recursive 종료
        return
    # 공백으로 바꾸기
    for i in range(startX + N // 3, startX + (N // 3) * 2):
        for j in range(startY + N // 3, startY + (N // 3) * 2):
            stars[i][j] = ' '
    
    # 재귀호출한다.
    for i in range(3): 
        for j in range(3):
            pattern(startX + i * N // 3, startY + j * N // 3, N // 3)
            

N = int(input())
stars = [["*"]*N for _ in range(N)] # 초기값 넣기
pattern(0, 0, N)

for i in range(N):
    print(''.join(stars[i]))