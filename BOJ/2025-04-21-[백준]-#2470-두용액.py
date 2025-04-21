import sys
input = sys.stdin.readline

"""
산성용액: 1 ~ 10**9
알칼리: -1 ~ -10**9
같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.

즉, 두 용액을 더한 값의 절댓값이 작아야 한다. -> 이에 해당하는 두 용액 찾아 출력해야 한다.
"""

N = int(input())  # 전체 용액의 수
liquid = sorted(map(int, input().split()))

left = 0
right = N - 1
answer = abs(liquid[left] + liquid[right])
answer_liquid = [liquid[left], liquid[right]]

while left < right:
    temp = liquid[left] + liquid[right]
    # 합이 0에 가까우면 정답 갱신
    if abs(temp) < answer:
        answer = abs(temp)
        answer_liquid = [liquid[left], liquid[right]]
    # 투 포인터 이동
    if temp < 0:
        left += 1
    else:
        right -= 1

print(answer_liquid[0], answer_liquid[1])