from sys import stdin

N = int(stdin.readline())
factorial = 1
for i in range(1,N+1):
    factorial *= i
print(factorial)