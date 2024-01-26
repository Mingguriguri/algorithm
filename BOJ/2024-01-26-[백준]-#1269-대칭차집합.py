from sys import stdin
cnt = 0
Anum, Bnum = map(int, stdin.readline().strip().split())
Ali = list(map(int, stdin.readline().strip().split()))
Bli = list(map(int, stdin.readline().strip().split()))

A = {}
B = {}

for i in range(Anum):
    A[Ali[i]] = 0
for i in range(Bnum):
    B[Bli[i]] = 0
print(A,B)
######################
for a in A.keys():
    # B-A
    if a in B:
        B[a] += 1

for b in B.keys():
    # A-B
    if b in A:
        A[b] += 1

for key, value in A.items():
    if value == 0:
        cnt += 1

for key, value in B.items():
    if value == 0:
        cnt += 1
print(cnt)