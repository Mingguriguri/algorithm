from sys import stdin
from collections import deque
N = int(stdin.readline()) # 명령의 수
# 덱 생성
deq = deque([])

for i in range(N):
    command = stdin.readline().split()
    # 1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
    if command[0] == "1":
        deq.appendleft(int(command[1]))
    # 2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
    elif command[0] == "2":
        deq.append(int(command[1]))
    #3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    elif command[0] == "3":
        if len(deq) > 0:
            print(deq.popleft())
        else:
            print(-1)
    #4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    elif command[0] == "4":
        if len(deq) > 0:
            print(deq.pop())
        else:
            print(-1)
    #5: 덱에 들어있는 정수의 개수를 출력한다.
    elif command[0] == "5":
        print(len(deq))
    #6: 덱이 비어있으면 1, 아니면 0을 출력한다.
    elif command[0] == "6":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    #7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    elif command[0] == "7":
        if len(deq) > 0:
            print(deq[0])
        else:
            print(-1)
    #8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    elif command[0] == "8":
        if len(deq) > 0:
            print(deq[len(deq)-1])
        else:
            print(-1)
