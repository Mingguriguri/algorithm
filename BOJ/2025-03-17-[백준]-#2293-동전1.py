import sys
input = sys.stdin.readline

'''
0이 입력되면 종료임
중점: 0
위쪽: 1
왼쪽: 2
아래: 3
오른: 4

두 발이 같은 지점에 있어선 안 됨
모든 지시 사항을 만족하는데 사용되는 "최소"의 힘
중앙에서 다른 지점으로 움직일 때, 위치에 따라 다른 힘을 사용함
- 중앙 -> 다른 지점: 2
- 어떤 지점 -> 인접한 지점 : 3
- 어떤 지점 -> 반대편: 4
- 같은 지점: 1

뭔가 스케줄링 느낌
 (0, 0) → (0, 1) → (2, 1) → (2, 1) → (2, 4) : 2 + 3 + 3 = 8
 (0, 0) → (0, 1) → (0, 2) → (0, 3) → (0, 4) : 2 + 2 + 2 + 2 = 8
 (0, 0) → (0, 1) → (2, 1) → (2, 1) → (1, 4) : 2 + 2 + 2 + 3 = 9

 
'''
INF = float("inf")
nums = list(map(int, input().split()))
#  0  1  2  3  4
# [1, 2, 4, 4, 0]
n = len(nums)
dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(n)]
# dp = [[INF] * n for _ in range(n)]
dp[0][0][0] = 0 # 초기값

def move(start, end):
    if start == 0 or end == 0: # 0을 거침
        return 2
    if start == end: # 같은 지점
        return 1
    if abs(start - end) % 2 == 0: # 짝수차이가 나면 반대지점
        return 4
    else:
        return 3

for i in range(n):
    for j in range(5):
        for k in range(5):
            if nums[i]


# for i in range(1, n-1):

    # if abs(current[0] - nums[i + 1]) % 2 == 0: # 짝수라면 반대지점, 홀수라면 인접 지점
    #     min_power[i] = min(min_power[i], 3)
    # else:
    #     min_power[i] = min(min_power[i], 4)
    # if abs(current[1] - nums[i + 1]) % 2 == 0:  # 짝수라면 반대지점, 홀수라면 인접 지점
    #     min_power[i] = min(min_power[i], 3)
    # else:
    #     min_power[i] = min(min_power[i], 4)

