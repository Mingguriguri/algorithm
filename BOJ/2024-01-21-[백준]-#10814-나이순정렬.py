from sys import stdin
n = int(stdin.readline())
users = []
for i in range(n):
    age, name = map(str, input().split())
    users.append([int(age), name])

users.sort(key = lambda x: x[0])

for i in range(n):
    print("%d %s"%(users[i][0], users[i][1]))