# 입력
n, m = map(int, input().split())
chess = [input() for _ in range(n)]
count = 0
color = 'B'
print(chess)

'''
아예 로직이 떠오르지 않아.........
한 줄씩 보면서 W 다음에는 B, B다음에는 W가 나오는지 확인한다.
이때 연속으로 같은 수가 나오면
M-8, N-8
'''
for i in range(n):
    for j in range(m):
        if chess[i][j] == color:
            color = 'W'
        
# 출력
print(count)