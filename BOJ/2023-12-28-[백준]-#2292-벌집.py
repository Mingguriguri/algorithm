n = int(input())
substract = 1
cnt = 1

while (n-substract) > 0:
    n -= substract
    substract = cnt * 6
    cnt += 1

print(cnt)