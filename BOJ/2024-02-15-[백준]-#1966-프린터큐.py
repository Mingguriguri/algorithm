from sys import stdin
from collections import deque

T = int(stdin.readline())
for _ in range(T):
    N, M = map(int, stdin.readline().strip().split())
    # 그 후, queue 덱에 문서들의 중요도를 입력받아 저장한다. 이때, enumerate()를 이용해 초기위치도 함께 저장한다.
    queue = deque(enumerate(map(int, stdin.readline().strip().split())))
    # 0: 초기위치 / 1: 중요도
    count = 0
    while True:
        #  queue의 첫번째 인덱스값의 중요도가 전체 queue의 중요도 중에 가장 큰 값인지 확인
        if queue[0][1] == max(queue, key=lambda x: x[1])[1]:
            count += 1 # 만약 큰 값이라면 count
            # 그리고 이 문서가 찾고자 하는 문서의 위치(M)에 해당하는지 확인
            if queue[0][0] == M: 
                print(count)
                break
            # 찾고자 하는 문서의 위치가 아니라면 어차피 가장 큰 값은 먼저 출력되어야 하므로 그냥 내보낸다. (popleft)
            else:
                queue.popleft()
        # 가장 큰 값이 아니라면 popleft하여 맨 뒤에 추가(append)한다.
        else:
            queue.append(queue.popleft())