from sys import stdin

def my_round(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)
n = int(stdin.readline())
levels = []
cnt = 0
avg = 0
if n != 0:
    cnt = my_round(n*0.15)
    for i in range(n):
        levels.append(int(stdin.readline()))
    # 정렬
    levels.sort()

    if cnt > 0:
    # 실제로 제거할 필요없이 평균값 낼 때 그 값을 빼고 하면 됨
        avg = my_round(sum(levels[cnt:-cnt]) / (n-2*cnt))
    else:
        avg = my_round(sum(levels)) // n
    print(avg)
else:
    print(0)
    
