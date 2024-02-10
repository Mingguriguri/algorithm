from sys import stdin

'''
여는 괄호인 경우 -> stack에 저장
닫는 괄호인 경우 -> stack에서 pop
이때 짝이 맞아야 하므로 닫는 괄호인 경우,
스택이 비어있지 않고, 여는 괄호와 짝이 맞는지 확인해야 한다. 
스택에 괄호가 아예 없을 경우 균형잡힌 문자열이므로 마지막에 스택의 길이가 0인지 판단한다.
'''
while True:
    string = input()
    stack = []
    flag = True 
    
    if string == '.':
        break

    for s in string:
        
        if s in '([':
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1] != '(':
                flag = False
                break
            else:
                stack.pop()
        elif s == ']':
            if not stack or stack[-1] != '[':
                flag = False
                break
            else:
                stack.pop()
           
    if flag and len(stack) == 0:
        print("yes")
    else:
        print("no")
