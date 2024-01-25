from sys import stdin
n, m = map(int, stdin.readline().strip().split())
check = []
cnt = 0
for _ in range(n):
    check.append(input())

for i in range(m):
    data = input()
    if data in check:
        cnt += 1
print(cnt)
