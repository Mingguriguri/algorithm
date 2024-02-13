from sys import stdin
from collections import deque

N = int(stdin.readline())
ballons = list(map(int, stdin.readline().strip().split()))
ballons = deque(enumerate(ballons))
answer = []
idx = 0

while len(ballons)>1:
    answer.append(ballons[0][0]+1)
    idx = ballons[0][1]
    ballons.popleft()
    if idx >= 0: #양수면
        for i in range(abs(idx)-1):
            ballons.append(ballons.popleft())
    else: #음수면
        for i in range(abs(idx)):
            ballons.appendleft(ballons.pop())
answer.append(ballons[0][0]+1)

for i in range(len(answer)):
    print(answer[i], end=' ')