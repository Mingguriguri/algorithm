m = int(input())
n = int(input())
min1 = 0
sum1 = 0

for num in range(m, n+1):
    if num > 1:
        if num == 2:
            min1 = 2
            sum1 += 2
        for j in range(2, num):
            if (num)%j == 0:
                break
            if num == j+1:
                if min1 == 0:
                    min1 = j+1
                sum1 += j+1

# output
if sum1 == 0:
    print(-1)
else:
    print(sum1)
    print(min1)