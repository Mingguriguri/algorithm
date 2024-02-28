import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().strip().split())
nums = [i for i in range(1, N+1)]
nPm = itertools.permutations(nums, M)

for i in nPm:
    for j in i:
        print(j, end=' ')
    print()