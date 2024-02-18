from sys import stdin
import math

N = int(stdin.readline())
for _ in range(N):
    west, east = map(int, stdin.readline().strip().split())
    if west == east:
        print(1)
    elif west < east:
        print(math.comb(east, west))