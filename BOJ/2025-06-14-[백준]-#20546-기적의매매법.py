import sys
input = sys.stdin.readline

money = int(input())
prices = list(map(int, input().split()))

"""
준현 (BNP)
매일 주식을 살 수 있다면 가능한 한 많이 산다 (매수는 전량, 매도 없음)
"""
jh_cash = money
jh_stock = 0
for price in prices:
    if jh_cash >= price:
        jh_stock += jh_cash // price
        jh_cash = jh_cash % price

jh_total = jh_cash + jh_stock * prices[-1]

"""
성민 (TIMING)
3일 연속 하락하면 → 전량 매수
3일 연속 상승하면 → 전량 매도
"""
sm_cash = money
sm_stock = 0
for i in range(3, 14):
    # 3일 연속 상승 -> 전량 매도
    if prices[i-3] < prices[i-2] < prices[i-1]:
        sm_cash += prices[i] * sm_stock
        sm_stock = 0
    # 3일 연속 하락 -> 전량 매수
    if prices[i-3] > prices[i-2] > prices[i-1]:
        sm_stock += sm_cash // prices[i]
        sm_cash = sm_cash % prices[i]

sm_total = sm_cash + sm_stock * prices[-1]

# 결과 출력
if jh_total > sm_total:
    print("BNP")
elif jh_total < sm_total:
    print("TIMING")
else:
    print("SAMESAME")