import sys
input = sys.stdin.readline

N = int(input())
divisor = list(map(int, input().rstrip().split()))

print(min(divisor)*max(divisor))