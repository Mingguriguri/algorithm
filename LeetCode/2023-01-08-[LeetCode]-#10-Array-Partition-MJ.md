# #10. Array Partition

progress: Not started
site: LeetCode
upload: No
등급: Easy
유형: 배열, 투 포인터/슬라이딩 윈도우
작성일시: 2023년 1월 8일 오후 9:12

# 📖Problems

Given an integer array `nums` of `2n` integers, group these integers into `n` pairs `(a1, b1), (a2, b2), ..., (an, bn)` such that the sum of `min(ai, bi)` for all `i` is **maximized**. Return *the maximized sum*.

**Example 1:**

```
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
```

**Example 2:**

```
Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.

```

**Constraints:**

- `1 <= n <= 104`
- `nums.length == 2 * n`
- `104 <= nums[i] <= 104`

# 🔍Solution

문제가 잘 이해가 가지 않는다. 문제를 번역해보자.

- 2n개 정수의 정수 배열 번호가 주어지면**, 모든 i에 대한 최소(ai, bi)의** **합이 최대가 되도록** 이 정수들을 n개의 쌍(a1, b1), (a2, b2), ..., (an, bn)으로 그룹화합니다. **최대화된 합계를 반환**합니다.

→ 즉, 그룹화하여 짝을 지은 **쌍들의 min()을 합산했을 때 최대**를 만드는 문제이다. 

예시로 들어온 [1, 4, 3, 2]로 분석해보자

이를 정렬을 한다면 [1, 2, 3, 4]가 된다. 각각의 쌍은 (1, 4)와 (2, 3), (1, 3)과 (2, 4), (1, 2)와 (3, 4)가 있다.

이들을 min()으로 한 후 합산해보자.

1. min(1, 4) + min(2, 3) = 1 + 2 = 3
2. min(1, 3) + min(2, 4) = 1 + 2 = 3
3. min(1, 2) + min(3, 4) = 1 + 3 = 4

따라서 이들 값들 중 가장 큰 값은 4이므로 4가 최대가 된다. 최대가 되는 4는 오름차순으로 정렬했을 때 최대가 되는 것을 볼 수 있다.

다른 예제도 마찬가지이다.

nums = [6,2,6,5,1,2]일때의 경우를 보자. 정렬하면 [ 1, 2, 2, 5, 6, 6]이며

min(1, 2) + min(2, 5), min(6, 6) = 1 + 2 + 6 = 9로 output과 일치하다.

이를 토대로 flow를 짜보겠다.

- min함수를 통해 더한 값을 저장할 `sum` 변수를 0으로 초기화한다. 각 쌍을 append할 리스트 `jjak`을 선언해준다. 이후, `nums`를 오름차순으로 정렬한다.
- 정렬한 `nums`의 `i`번째부터 `jjak`에 append하여 쌍을 이룬다.
- 이후 min값을 구한 값을 `sum`에 저장한다. 다시 `jjak`리스트를 초기화한 후, 다음 쌍을 만들어준다.
- 위 과정을 `nums`리스트가 끝날 때까지 반복한다.
- `sum`을 반환한다.

## 🚩My submission

```python
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        jjak = []
        nums.sort()

        for i in nums:
            # 앞에서부터 오름차순으로 짝을 만들어 합 계산
            jjak.append(i)
            if len(jjak) == 2:
                sum += min(jjak)
                jjak = []

        return sum
```

![561 solve.JPG](#10%20Array%20Partition%208cb9fa3cac344bd0b982a85329443d8e/561_solve.jpg)

## 🚩Others submission

1. **짝수번째 값 계산**
- 쌍은 짝수 번째 값부터 시작한다. 따라서 min()을 구하지 않더라도 짝수 번째 값을 더하면 된다.
- 정렬된 상태에서는 짝수번째에 항상 작은 값이 위치한다.

```python
class Solution(object):
    def arrayPairSum(self, nums):
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n
        return sum
```

![solve2.JPG](#10%20Array%20Partition%208cb9fa3cac344bd0b982a85329443d8e/solve2.jpg)

- 아이디어를 생각해내면 훨씬 더 단순해지는 것 같다.
- 문제에서 `min()`을 쓰라는 느낌을 받아서 이 방식은 생각 못했을 것 같다.
- 코드는 간결하고 보기 쉽다. 하지만 런타임 자체는 위와 비슷하다.

1. **슬라이싱을 이용한 파이썬다운 방식**

슬라이싱을 활용하면 단 한 줄로 풀이할 수 있다. ***(Pythonic Way)***

```python
class Solution(object):
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])
```

![solve3.JPG](#10%20Array%20Partition%208cb9fa3cac344bd0b982a85329443d8e/solve3.jpg)

- 이전 1번처럼 결국엔 짝수값을 더하는 것이기 때문에 슬라이싱을 통해 2씩 더하면 끝난다.

→ 런타임이나 메모리는 3방법 모두 크게 차이가 없다.

# 💡Retrospect 회고

- 오름차순으로 만들어 푸는 것까지 되게 오래걸렸는데 조금 더 고민하고 조금 더 문제의 패턴을 파악한다면 더 쉽게 코드를 짤 수 있다는 것을 알게 되었다.

# 🎯Reference

- 파이썬 알고리즘 인터뷰_ 191p-192p