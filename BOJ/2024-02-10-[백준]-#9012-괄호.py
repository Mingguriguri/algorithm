from sys import stdin
N = int(stdin.readline()) # 명령의 수
stack = []

for i in range(N):
    stack = []
    brackets = stdin.readline().strip()
    for b in brackets:
        if b == '(':
            stack.append(b)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(b)
    if len(stack) == 0: #스택이 비어있다면 괄호의 짝이 다 맞는 것
        print("YES") 
    else: # 그게 아니라 스택에 값이 하나라도 있다면 NO
        print("NO")