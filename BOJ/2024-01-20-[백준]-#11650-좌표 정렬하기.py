from sys import stdin
n = int(stdin.readline())
xy = [0]*n

for i in range(n):
    x, y = map(int, stdin.readline().split())
    xy[i] = [x,y]

xy.sort(key=lambda x :(x[0], x[1]))

for i in range(n):
    print("%d %d"%(xy[i][0], xy[i][1]))

