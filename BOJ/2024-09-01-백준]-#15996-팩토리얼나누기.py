import sys
input = sys.stdin.readline

N, A = map(int, input().split())
k = 0
power = A
while N >= power:
    k += N // power
    print(f"k = {k}, power = {power}", end='')
    power *= A
    print(f"   power:{power}")

print(k)
