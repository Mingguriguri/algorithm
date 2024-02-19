from sys import stdin

N = int(stdin.readline())
times = list(map(int, stdin.readline().strip().split()))
times.sort()
outsum = 0
for i in range(len(times)):
    insum = 0
    for j in range(i+1):
        insum += times[j]
    outsum += insum
print(outsum)