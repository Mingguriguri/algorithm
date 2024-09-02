import sys
input = sys.stdin.readline

# N: 온도 측정 전체 날짜. K: 합을 구하기 위한 연속적인 날짜 수
N, K = map(int, input().split())
temps = list(map(int, input().split())) # 온도 정수 수열
prefix_sum = [0] * (N - K + 1)

for i in range(len(prefix_sum)):
    prefix_sum[i] = sum(temps[i:i + K])

print(max(prefix_sum))