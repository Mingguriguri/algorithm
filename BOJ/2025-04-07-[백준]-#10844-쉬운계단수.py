import sys
input = sys.stdin.readline

'''
DP에는 길이가 i고 j가 마지막 수의 개수가 저장되어야 한다.
'''

N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % 1000000000)