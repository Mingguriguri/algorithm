import sys
input = sys.stdin.readline

N = int(input().strip())  # kg

# 5kg 봉지 최대한 많이 사용
bag_count = 0

while N >= 0:
    if N % 5 == 0:  # 5의 배수인 경우
        bag_count += N // 5
        print(bag_count)
        break
    N -= 3
    bag_count += 1
else:
    print(-1)