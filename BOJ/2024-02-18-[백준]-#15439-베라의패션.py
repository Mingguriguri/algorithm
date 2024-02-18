from sys import stdin
from itertools import permutations

N = int(stdin.readline())
# print(list(permutations(range(N),2)))
# N = 5
# [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3)]
# 20
print(len(list(permutations(range(N),2))))

# n = int(input())
# print(n*(n-1))