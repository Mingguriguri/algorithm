from sys import stdin
n = int(stdin.readline())
li=[]
for i in range(n):
    li.append(int(stdin.readline()))

li.sort()
for i in li:
    print(i)