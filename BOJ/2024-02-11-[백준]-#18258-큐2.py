from sys import stdin
from collections import deque
N = int(stdin.readline()) # 명령의 수
queue = deque([])
for i in range(N):
    request = stdin.readline().split()
    if request[0] == 'push': #정수 X를 큐에 넣는 연산
        queue.append(request[1])
    elif request[0] == 'pop': # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력 (없는 경우에는 -1)
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif request[0] == 'size': #  큐에 들어있는 정수의 개수
        print(len(queue))
    elif request[0] == 'empty': # 큐가 비어있으면 1, 아니면 0
        if not queue:
            print(1)
        else:
            print(0)
    elif request[0] == 'front': #큐의 가장 앞에 있는 정수를 출력(앖으면 -1)
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif request[0] == 'back': # 큐의 가장 뒤에 있는 정수를 출력(없으면 -1)
        if queue:
            print(queue[-1])
        else:
            print(-1)