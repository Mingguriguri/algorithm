from sys import stdin
K = int(stdin.readline())
stack = []

for i in range(K):
    n = int(stdin.readline())
    if n == 0 and len(stack)>0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))