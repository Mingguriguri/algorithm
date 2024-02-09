from sys import stdin
N = int(stdin.readline()) # 명령의 수
stack = []

for i in range(N):
    request = stdin.readline().split()
    if request[0] == '1':
        stack.append(request[1])
    elif request[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif request[0] == '3':
        print(len(stack))
    elif request[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif request[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)