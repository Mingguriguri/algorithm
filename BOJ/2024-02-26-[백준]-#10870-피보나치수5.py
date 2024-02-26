import sys
input = sys.stdin.readline

def fibo(N):
    if N <= 1:
        return N
    else:
        return fibo(N-1)+fibo(N-2)

N = int(input())
print(fibo(N))