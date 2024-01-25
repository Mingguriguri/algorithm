from sys import stdin
n = int(stdin.readline())
company = {}
stack=[]
for _ in range(n):
    name, status = map(str, input().split()) 
    company[name] = status
# value값이 enter인 경우( = 아직 회사에 있는 사람)
# stack에 key값을 push
for key, value in company.items():
    if value == 'enter':
        stack.append(key)

# 사전 역순 정렬
stack.sort(reverse=True)
# 한 줄에 한 명씩 출력
for stk in stack:
    print(stk)
