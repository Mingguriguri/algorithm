
# [프로그래머스 - 고득점 kit - 스택/큐 - 주식가격](https://school.programmers.co.kr/learn/courses/30/lessons/42584)

# 📖Problems

초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

**제한사항**

- prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
- prices의 길이는 2 이상 100,000 이하입니다.

**입출력 예**

| prices | return |
| --- | --- |
| [1, 2, 3, 2, 3] | [4, 3, 1, 1, 0] |

**입출력 예 설명**

- 1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
- 2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
- 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
- 4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
- 5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

# 🔍Institution

스택

# 🔍Approach

## 🚩My submission

**Flow**

1. s`tack = [], answer = [], second = 1`
2. 3~4 까지 for문을 돌면서 `prices`의 각 인덱스별로 살펴본다.
3. `stack`안에 아무것도 없다면, 인덱스 `i`와 `prices[i]`를 `stack`에 함께 append한다.  
4. `stack`의 마지막 값보다 크다면, 인덱스`i`와 prices[i]를 `stack`에 함께 append한다. 만약 그게 아니라면 `pop`하고 `stack`에 있는 인덱스를 `answer`의 `i`번째 값에 기본 default초인 1을 넣는다.
5. for문을 다 돌면서 `stack`에 채워넣었다면, 다시 for문을 새로 돌면서 stack에 있는 요소들을 pop한 후 `answer`에 채워넣는다.
    1. 스택의 길이와 같이 저장한 인덱스간의 차이가 곧 시간이므로, `answer[stack[-1][0]] = len(stack)-stack.pop()[0]`
    
    ```python
    def solution(prices):
        stack = []
        answer = [0] * len(prices)
        
        for idx, nums in enumerate(prices):
            if not stack:
                stack.append([idx, nums])
                continue
            if stack[-1][1] <= nums:
                stack.append([idx, nums])
            else:
                answer[stack.pop()[0]] = 1
                stack.append([idx,nums])
        # for문을 다 돌았다면
        stack_length = len(stack)
        for _ in range(stack_length):
            last = stack.pop()[0] 
            answer[last] = stack_length - last
            # answer[stack[-1][0]] = stack_length - stack.pop()[0]
        
        return answer
    ```
  
  
![%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2023-01-19_21-55-21](https://user-images.githubusercontent.com/101111603/221585466-9f4833bc-4aa3-4b2c-bcc1-ecdb12b6b053.png)

![%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2023-01-19_21-56-02](https://user-images.githubusercontent.com/101111603/221585502-2dbb0604-8374-4cdb-b202-73fac9272f72.png)

    
  테스트케이스는 잘 작동하는데, 제출하면 완전히 틀려버린다. 이유가 도대체 뭐지..!?!
  
  
    
    **풀이 보완**
    
    참고한 사이트 : 
    
    ```python
    def solution(prices):
        
        answer = [0] * len(prices)
        stack = []
        
        for idx, p in enumerate(prices):
            while stack and (p < prices[stack[-1]] or idx == len(prices)-1):
                last = stack.pop()
                answer[last] = idx - last
            stack.append(idx)
        
        
        return answer
    ```
    
    Time coplexity: O(n)
    
    **Space complexity: O(n) + O(n) = O(2n) = O(n)**
    

## 🚩Others submission

1. brute force 

```python
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer
```

Time coplexity: O(n)

**Space complexity: O(n) + O(n) = O(2n) = O(n)**

1. queue

```python
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer
```

Time coplexity: O(n)

**Space complexity: O(n) + O(n) = O(2n) = O(n)**

1. stack

```python
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer
```

Time coplexity: O(n)

**Space complexity: O(n) + O(n) = O(2n) = O(n)**
