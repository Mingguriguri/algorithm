# 힙 - 더 맵게

progress: Done
review: 🥜
site: 프로그래머스
upload: Yes
등급: Level2
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42626
알고리즘 개념: https://www.notion.so/Heap-0534d479740040a195d844181b898108
유형: 힙
작성일시: 2023년 1월 24일 오전 11:04

# [프로그래머스 - 코딩테스트 연습 - 고득점 kit - 힙 - #.더 맵게](https://school.programmers.co.kr/learn/courses/30/lessons/42626)

# 📖Problems

매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

`섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)`

Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

### 제한 사항

- scoville의 길이는 2 이상 1,000,000 이하입니다.
- K는 0 이상 1,000,000,000 이하입니다.
- scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
- 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

### 입출력 예

| scoville | K | return |
| --- | --- | --- |
| [1, 2, 3, 9, 10, 12] | 7 | 2 |

### 입출력 예 설명

1. 스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]
2. 스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13가진 음식의 스코빌 지수 = [13, 9, 10, 12]

모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.

# 🔍Institution

이 문제는 ‘힙’ 유형에 있으므로 힙을 이용한다.

힙 구조 : 최댓값과 최솟값을 빠르게 찾기 위해 고안된 자료구조이다.

파이썬에서는 힙을 굳이 구현하지 않더라도 heapq를 import하면 push, pop, 정렬 등 자동으로 가능하다.

```python
import heapq #heap 알고리즘 사용 시 import

i_list = []
heapq.heapify(i_list) #i_list를 heapify (힙 알고리즘 적용)
heapq.heappush(i_list, element) #heap에 push할 땐 list와 element를 인자로 갖는 heappus사용
heapq.heappop(i_list) #heap에서 가장 작은 값을 삭제할 때 heappop()을 사용
```

# 🔍Approach

1. scoville 리스트를 heapify 시킨다.
2. **언제 pop?**
heapify로 정렬된 scoville에서 가장 작은 수와 두번째로 작은 수가 K보다 작을 때, 이 두 수를 pop한다.
3. **무엇을 추가?**
pop한 후에 주어진 공식으로 연산된 scoville 값을 push한다.

## 🚩My submission

🚩**최종 수정 flow**

1. `scoville`리스트와 `K`를 입력받는다. `answer`는 스코빌 지수를 K이상으로 만들기 위해 섞어야 하는 최소 횟수이다. 따라서 섞을 때마다 `answer`에 1을 더한다.
2. `heapq.heapify(scoville)`을 통해서 `scoville`리스트를 힙 알고리즘을 적용한다. 
(heapify를 사용하면 자동으로 정렬이 된다.)
3. `scoville`의 가장 앞에 있는 값(가장 작은 값)이 K보다 크거나 같다면, 이미 `scoville`지수가 `k`이상이 되었으므로 **더 연산할 필요 없이 바로 `answer`를 return한다.**
4. 그게 아니라면 반복하여 아래 연산을 수행한다.
    - **가장 작은 수와 두 번째로 작은 수를 pop해서 mix_scoville 변수에 공식을 적용한 후 저장한다. 
    `mix_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)`**
    - **섞을 때마다 `answer`에 1을 더한다.**
    - `**mix_scoville`을 `scoville` heapq에 push한다.**
5. 위 과정을 `scoville`의 길이가 0이 될 때가지 반복한다. 
(지속적으로 scoville을 pop하여 연산을 수행하며, 만약 연산이 다 되었다면 중간에 return하기 때문에 굳이 while True를 할 필요가 없다)
6. `scoville`의 가장 작은 값 (`scoville[0]`)이 `K`보다 크거나 같다면 `answer`를 return하고 그것이 아니라면 `-1`을 return한다.

**결과**

```python
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:

        if scoville[0] >= K:
            return answer
        mix_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        answer += 1
        heapq.heappush(scoville, mix_scoville)

    if scoville[0] >= K:
        return answer
    else:
        return -1
```

![스크린샷, 2023-01-24 11-46-20.png](%E1%84%92%E1%85%B5%E1%86%B8%20-%20%E1%84%83%E1%85%A5%20%E1%84%86%E1%85%A2%E1%86%B8%E1%84%80%E1%85%A6%20b695d17ee7994b78a6751508d0aa3ae2/%25EC%258A%25A4%25ED%2581%25AC%25EB%25A6%25B0%25EC%2583%25B7_2023-01-24_11-46-20.png)

🚩**초기** **Flow**

1. `scoville`리스트와 `K`를 입력받는다. `answer`는 스코빌 지수를 `K`이상으로 만들기 위해 섞어야 하는 최소 횟수이다. 따라서 섞을 때마다 `answer`에 1을 더한다.
2. `heapq.heapify(scoville)`을 통해서 `scoville`리스트를 힙 알고리즘을 적용한다.
3. index 0번과1번이 K보다 작을 때 이 두 수를 pop해서 `mix_scoville` 변수에 공식을 적용한 후 저장한다. `mix_scoville = scoville.pop(0) + (scoville.pop(0) * 2)`
4. 섞을 때 `answer` 에 1을 더해준다.
5. 이 `mix_scoville`의 값을 `scoville`리스트에 append한다.
6. 2~5번까지 while True를 통해 반복수행한다. 스코빌지수가 모두 `K`이상일 때 break한다.
7. 반복이 끝나면 `answer`를 return한다.

🚩**1차 시도**

```python
import heapq

def solution(scoville, K):
    answer = 0
    
heapq.heapify(scoville)   
while True:
               
        if scoville[0] < K and scoville[1] < K:
            mix_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
            answer += 1
            heapq.heappush(scoville, mix_scoville)
        
        if scoville[0] > K:
            return answer
            break
        
    return -1
```

코드 실행 >> 통과

제출 >>

![스크린샷, 2023-01-24 11-36-27.png](%E1%84%92%E1%85%B5%E1%86%B8%20-%20%E1%84%83%E1%85%A5%20%E1%84%86%E1%85%A2%E1%86%B8%E1%84%80%E1%85%A6%20b695d17ee7994b78a6751508d0aa3ae2/%25EC%258A%25A4%25ED%2581%25AC%25EB%25A6%25B0%25EC%2583%25B7_2023-01-24_11-36-27.png)

이유 : while 문 안에 자꾸 heapify를 시켜 너무 많은 연산이 수행되었다.

**2차 시도**

- heapify를 while문 밖에서 실행시켰다.
- 조건을 수정하였다.
    - `scoville[0]`과 `scoville[1]`이 `K`보다 작은 경우를 지웠다.
    - 무한반복에 종료조건으로 `scoville[0]`의 값이 `K`보다 크거나 같다면 `answer`를 return하고 종료하도록 하였다.
    - 또한 스코빌 지수를 섞는 연산은 while안에 있다면 계속 반복 수행하도록 하였다.

```python
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        
        if scoville[0] >= K:
            return answer
        mix_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        answer += 1
        heapq.heappush(scoville, mix_scoville)

    if scoville[0] >= K:
        return answer

    else:
        return -1
```

코드 실행 >> 통과

제출 >>

![스크린샷, 2023-01-24 11-42-37.png](%E1%84%92%E1%85%B5%E1%86%B8%20-%20%E1%84%83%E1%85%A5%20%E1%84%86%E1%85%A2%E1%86%B8%E1%84%80%E1%85%A6%20b695d17ee7994b78a6751508d0aa3ae2/%25EC%258A%25A4%25ED%2581%25AC%25EB%25A6%25B0%25EC%2583%25B7_2023-01-24_11-42-37.png)

**런타임에러 >> index out of range 인 경우가 많다. 이는 반복문과 관련하여 무언가가 잘못 되었을 확률이 크다.**

- 따라서 while문의 조건을 재설정하였다.
- 무한 반복이 아니라, `scoville`리스트의 길이가 0이 되기 전까지 반복되도록 하였다. 
만약 `scoville[0]`이 `K`보다 작다면 계속 연산을 수행해야 하고, 그럴 때마다 list의 값이 pop되기 때문이다.

**마지막 시도**

- 자세한 설명 및 flow는 위에 있습니다.

```python
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:
        
        if scoville[0] >= K:
            return answer
        mix_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        answer += 1
        heapq.heappush(scoville, mix_scoville)

    if scoville[0] >= K:
        return answer
    else:
        return -1
```

코드 실행 >> 통과

제출 >> 통과

## 🚩Others submission

```python
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
```

- 무한 반복을 사용하였기 때문에 종료조건을 걸어주었다.
- 내 풀이와 비슷하지만, 내가 놓쳤던 부분을 확인할 수 있었다. while True를 사용했을 때 종료조건은 최대한 상세히 적어야 한다.

```python
from heapq import heapify, heappush, heappop
def solution(scoville, K):
    heapify(scoville)
    for i in range(1000000):
        try:
            heappush(scoville, heappop(scoville)+(heappop(scoville)*2))
            if scoville[0] >= K: return i+1
        except:
            return -1
```

- while이 아니라 for문을 통해서, 그리고 try, except를 이용한 코드이다.
- 한 줄에 다 적은 것이 인상적이었다.

# 💡Retrospect

- 스터디 하기 전에 힙에 대해 조금 예습을 했었다. 힙이란 무엇인지, 어떻게 구현하는지에 대해 찾아보았다. 하지만 막상 스터디에서 보니 파이썬에서는 힙을 미리 구현이 되어 있는 heapq를 import하면 굳이 코드를 작성하지 않아도 되었다. 이 부분이 정말 편한 것 같다.
    - 힙 관련 예습 자료 추천 : [나동빈 - ****11강 - 힙 정렬(Heap Sort) [ 실전 알고리즘 강좌(Algorithm Programming Tutorial) #11 ]****](https://youtu.be/iyl9bfp_8ag)
- 파이썬에서 힙을 사용할 때는 아래 코드들을 기억하자
    
    ```python
    import heapq #heap 알고리즘 사용 시 import
    
    i_list = []
    heapq.heapify(i_list) #i_list를 heapify (힙 알고리즘 적용)
    heapq.heappush(i_list, element) #heap에 push할 땐 list와 element를 인자로 갖는 heappus사용
    heapq.heappop(i_list) #heap에서 가장 작은 값을 삭제할 때 heappop()을 사용
    ```
    
- 다른 괜찮은 코드들도 많았지만 내가 보기엔 내가 짠 코드가 제일 괜찮은 것 같다.