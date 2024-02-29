import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().strip().split())))
for _ in range(N):
    B.append(list(map(int, input().strip().split())))

for i in range(N):
    for j in range(M):
        A[i][j] += B[i][j]

for i in range(N):
    print(' '.join(map(str, A[i])))