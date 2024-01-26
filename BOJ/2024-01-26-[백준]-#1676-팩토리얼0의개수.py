from sys import stdin
n = int(stdin.readline())
factorial = 1
cnt = 0
for i in range(1, n+1):
    factorial *= i

while True:
    if factorial % 10 == 0:
        factorial //= 10
        cnt += 1
    else:
        break
print(cnt)