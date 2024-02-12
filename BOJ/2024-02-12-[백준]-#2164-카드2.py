from sys import stdin
from collections import deque
N = int(stdin.readline())
cards=[]
if N == 1: # N이 1인 경우의 예외처리
    print(1)
else:
    # cards 리스트 1~N까지 채우기
    for i in range(1, N+1):
        cards.append(i)
    # cards 리스트를 deque 자료형으로 바꾸기
    cardsQueue = deque(cards)
    while cardsQueue:
    # 처음에는 popleft
        cardsQueue.popleft()
    # 길이가 1보다 크다면, popleft하여 맨 뒤에 append
        if len(cardsQueue) > 1:
            cardsQueue.append(cardsQueue.popleft())
    # 그게 아니라면 반복 종료
        else:
            break
    print(cardsQueue[0])