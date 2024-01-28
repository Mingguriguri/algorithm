from sys import stdin
n, m = map(int, stdin.readline().strip().split())
answer = []
#n: 듣도 못한 사람
#m: 보도 못한 사람
DBJ = {} # 듣도 보도 못한 사람
for i in range(n):
    DBJ[input()] = 0
for j in range(m):
    name = stdin.readline().strip()
    if name in DBJ:
        DBJ[name] += 1

for key, value in DBJ.items():
    if value >= 1:
        answer.append(key)

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)