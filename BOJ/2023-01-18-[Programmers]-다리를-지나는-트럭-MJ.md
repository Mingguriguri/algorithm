# 다리를 지나는 트럭

progress: Done
review: 🥜
site: 프로그래머스
upload: Yes
등급: Level2
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42583
유형: 스택/큐
작성일시: 2023년 1월 18일 오후 1:31

# [#**스택/큐 - 다리를 지나는 트럭(Level.2)**](https://school.programmers.co.kr/learn/courses/30/lessons/42583)

이 문제는 백준([#13335. 트럭](https://www.acmicpc.net/problem/13335))에도 있는 문제이다.

# 📖Problems

트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 `bridge_length`대 올라갈 수 있으며, 다리는 `weight` 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

| 경과 시간 | 다리를 지난 트럭 | 다리를 건너는 트럭 | 대기 트럭 |
| --- | --- | --- | --- |
| 0 | [] | [] | [7,4,5,6] |
| 1~2 | [] | [7] | [4,5,6] |
| 3 | [7] | [4] | [5,6] |
| 4 | [7] | [4,5] | [6] |
| 5 | [7,4] | [5] | [6] |
| 6~7 | [7,4,5] | [6] | [] |
| 8 | [7,4,5,6] | [] | [] |

따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

**제한 조건**

- bridge_length는 1 이상 10,000 이하입니다.
- weight는 1 이상 10,000 이하입니다.
- truck_weights의 길이는 1 이상 10,000 이하입니다.
- 모든 트럭의 무게는 1 이상 weight 이하입니다.

**입출력 예**

| bridge_length | weight | truck_weights | return |
| --- | --- | --- | --- |
| 2 | 10 | [7,4,5,6] | 8 |
| 100 | 100 | [10] | 101 |
| 100 | 100 | [10,10,10,10,10,10,10,10,10,10] | 110 |

# 🔍Institution

**트럭 여러대, 일차선 다리에 정해진 순으로 건넘, 다리를 건널 때 몇 초가 걸리는지 알아야 함**

- input : 트럭weight, bridge_lenth, weight
- 다리길이 = 걸리는 시간
- **목적 : 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내기**
- 문제유형 : Queue(FIFO) : 대기 중인 트럭들이 대기 순서에 맞게, 순서대로 건너야 함.
- 고려해야 할 것
    - 스택의 경우, 스택 안에 무엇을 넣어야 할지, 무엇을 pop할지 고려했었음
    - 마찬가지로 큐도 **무엇을 추가(push)할지, 언제 제거(pop)할지, 언제까지 반복할지** 고려해야 함

# 🔍Approach

큐

- 무엇을 추가? 트럭 무게
- 언제 제거? 트럭이 다리를 건넜을 때(=다리길이만큼의 초가 지났을 때)
- 언제까지 반복? 마지막 트럭이 다리를 건넜을 때

## 🚩My submission

- **flow**
1. `bridge_length`는 다리길이, 즉 경과시간을 더할 때 사용하는 값이며, `weight`은 다리가 견딜 수 있는 무게, `truck_weights` 는 트럭의 무게가 있는 리스트이다. `answer`에는 경과시간을 저장하여 returun한다.
2. `queue` 리스트를 만든다. `complete` 리스트는 다리를 지나는 트럭을 담는 리스트이다. `truck_weights`의 길이를 `truck_len`에 미리 저장한다.
3. for문을 통해 `queue`에 `truck_weights`을 집어넣는다. 이때, `weight`의 값이 넘어간다면 집어넣지 않는다. 집어넣은 트럭을 pop하고, `answer`에 `bridge_length`를 더한 후, 그 다음 `truck_weight`을 push한다.
    1. `answer`에 `bridge_lenth`를 더했다면, `queue`에 있는 값을 `pop`하고 이를 `complete`에 저장한다.
4. 마지막 트럭도 지나간다면, 즉 다리를 지난 트럭 리스트인 `complete`리스트의 길이가 `truck_len`와 같을 경우 반복을 종료한다.

```python
def solution(bridge_length, weight, truck_weights):
    truck_len = len(truck_weights)
    queue = []
    complete = []
    answer = 0
    i = 0
    while len(complete) != truck_len:
        if sum(queue) + truck_weights[i] <= weight:
            queue.append(truck_weights[i])
            continue
        else:
            complete.append(queue.pop(0))
            answer += bridge_lenth
        queue.append(truck_weights[i])
        i += 1
return answer
```

>> 실행 시간이 10.0초를 초과하여 실행이 중단되었습니다. 실행 시간이 더 짧은 다른 방법을 찾아보세요.

=> continue가 계속 들어가게 됨

2차 시도

```python
def solution(bridge_length, weight, truck_weights):
    truck_len = len(truck_weights)
    queue = []
    complete = []
    i, answer = 0, 0
    
    while len(complete) != truck_len:

        if sum(queue) + truck_weights[i] <= weight:
            queue.append(truck_weights[i])
        else:
            complete.append(queue.pop(0))
            answer += bridge_length
            i += 1

    return answer
```

테스트케이스1만 통과

## 🚩Others submission

[백준](https://fre2-dom.tistory.com/432)

```python
import sys

n, w, l = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
temp = [0] * w # 다리의 칸
cnt = 0

# 반복문을 통해 다리의 모든 트럭이 지나갈 때까지 반복
while temp:
    cnt += 1 # 카운트
    temp.pop(0) # 다리의 칸을 하나씩 줄인다.

    # 모든 트럭을 확인
    if a:
        # 현재 다리에 있는 트럭과 다리를 건너려는 트럭의 무게가
        # 다리의 하중보다 크다면 빈 공간을 추가
        if sum(temp) + a[0] > l:
            temp.append(0)

        # 다리의 하중보다 작다면 트럭을 다리에 추가
        else:
            temp.append(a.pop(0))

print(cnt)
```

- **무엇을 언제 추가(Push)할까?**

무엇: Truck의 weight와 다리를 올랐을 때의 시간

언제: 다리위에 있는 Truck들의 총 무게 + 현 Truck의 무게가 최대 무게보다 작거나 같을 때

- **언제 제거(Pop)할까?**

언제: Truck이 다리를 건너는데 걸리는 시간은? → bridge_length

현재시간 - Truck이 다리를 올랐을 때의 시간이 bridge_length보다 크거나 같을 때

- **언제까지 반복할까?**

대기트럭이 없을 때 까지 → 마지막 트럭이 다리를 건너는 시간을 고려해줘야 함

다리를 건너는 트럭이 없을 때 까지 = 다리를 지난 트럭의 개수가 처음의 대기트럭과 같을 때 까지

```python
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0

    while truck_weights: # 대기트럭 없을때까지
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[0] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop(0) -> 7
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step
```