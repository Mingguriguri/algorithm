# 내 풀이
from sys import stdin
from collections import deque
N, K = map(int, stdin.readline().split())
# 초기화
people = []
for i in range(1, N+1):
    people.append(i)
people = deque(people)
key = K-1
josep = []

# 풀이과정
# 1. key값에 해당하는 people리스트의 값을 josep에 추가하며, 
# 2. 해당 값은 people리스트에서 제거
# 3. key값 업데이트
# 4. 만약 people리스트의 길이가 1이하가 되면 마지막 key값만 추가
while len(people)>1:
    josep.append(people[key])
    del people[key]
    key = (key + K - 1) % len(people)
else:
    josep.append(people[key])
# 출력
print("<", end="")
for i in range(len(josep)-1):
    print("%d, "%josep[i], end="")
print("%d>"%josep[-1])