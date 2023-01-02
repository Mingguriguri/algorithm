# #198. House Robber

progress: Not started
review: 🥜
site: LeetCode
upload: No
등급: Medium
링크: https://leetcode.com/problems/house-robber/
알고리즘 개념: https://www.notion.so/DP-cb86236f695748e38b10b19d7eb5a68e
유형: 동적프로그래밍
작성일시: 2023년 1월 2일 오전 11:38

# 📖Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return *the maximum amount of money you can rob tonight **without alerting the police***.

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

```

**Example 2:**

```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

```

**Constraints:**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

# 🧐Institution

- I**nput: 각 집에 있는 돈이 1차원 array 형태**
- **Output: 훔칠 수 있는 돈의 최대값**
- **Constraint: 인접한 집일 경우 훔칠 수 없음**
- **접근 방법 : DP**
    - DP를 생각하게 된 이유는 이전에 백준 문제 중 [평범한 배낭]과 유사하다고 느꼈기 때문이다. 평범한 배낭 문제에서도 각각의 가치 중 최대가 되는 것을 구해야 했고 이때 DP를 사용해서 문제를 해결하였다. 냅색 알고리즘은 아래와 같은 방법으로 문제를 해결한다.
        1. j**가 현재 물건 무게 W보다 작을 때**
            - 현재 물건을 담을 수 없음 → 이전의 값 복사
                
                ```python
                dp[i][j] = dp[i-1][j]
                ```
                
        2. j**가 현재 물건의 무게 W와 같거나 클 때**
            - 현재 물건 담을 수 있다.
            - 물건을 담았을 때와 담지 않았을 때의 가치를 비교해준 뒤 더 큰 값을 할당한다.
            - 현재 물건의 가치는 V이다.
                
                ```python
                dp[i][j] = max( dp[i-1][j] , dp[i-1][j-w] + v)
                ```
                
        3. 따라서 물건의 **최대 가치**는 **`dp[가방크기][물건개수]`**로 구할 수 있다.
    - 이 방법을 참고하여 house robber문제에 적용하였다.

# 🔍Approach

1. **DP로 한다면 index와 value에는 어떤 값이 들어가야 할까?**
    - index : turn 횟수
    - value : 최대 돈 가치
    
2. **나열한 후에 점화식을 구해보자.**

nums = [2, 7, 9, 3, 1]

| index | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| values | 2 | 7 | 9 | 3 | 1 |

**dp[]**

| index | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| 최대 돈 가치 | 0 | nums[0] = 2 | 7+0=7 | 11 | 11 | 12 |

(여기서 `dp[0] = 0`인 이유는 i=2일때부터 앞의 값을 참고하여야 하기 때문에 0으로 초기화한다.)

**최댓값이 나올 수 있는 케이스를 먼저 따져보자** 

- **2 : 2 (idx0)**
- **7 : 7(idx1)**
- **9 : 9(idx2)**
- **3 : 3(idx3)+7(idx1)**
- **1 : 1(idx 4) + 9(idx 2) + 2(idx0)**

→ **dp[1] = num[0]**

→ **i=2부터 시작, max( dp[i-1], nums[i-1] +dp[i-2] )**

1. **dp[0] = 0**
2. **dp[1] = nums[0] = 2**
3. **dp[2] =max(2, 7+0) = max(7,0) = 7**
4. **dp[3] = max(7, 9+2) = max(7, 11) = 11**
5. **dp[4] =max(11, 3+7) = max(11, 10) = 11**
6. **dp[5] = max(11, 1+11) = max(11,12) = 12**

## My submission

### 🚩Try 1

```python
class Solution:
   def rob(self, nums):
'''
1. dp 리스트 초기화
2. dp에는 rob에 해당하는 최대 가치가 저장된다. 
3. dp[0]과 dp[1]은 rob[0]과 rob[1]자기 자신이 곧 최대이므로 미리 넣어준다.
4. 인접한 인덱스는 들리면 안 되므로 dp에 저장된 직전 인덱스, 즉 dp[i-2]와 rob에 있는 rob[i]를 더한 값과 직전에 저장한 dp[i-1]값을 비교한 후 큰 값을 다시 dp에 저장한다.	
5. dp의 마지막 인덱스에 있는 값을 출력한다.
'''
  dp = [0] * len(nums)+1
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
           
        return dp[-1]
```

**Results** : run하면 잘 실행되는데 submit 하면 `runtime error`

**Reason** 

- 문제에서 주어진 `constraints`를 다시 살펴보자
    - **Constraints:**
        - 1 <= nums.length <= 100
        - 0 <= nums[i] <= 400
    - 여기서 보면 nums.length가 1인 경우를 생각했을 때, index에 1을 넣어주게 된다면 index out of range 에러가 발생한다. 따라서 dp[1]에 nums[1] 값을 넣어준 것이 문제가 된 것이다.
        - ex) nums = [2], nums[1] = 없음 → index out of range
    - 따라서, nums[1]을 미리 넣지 않는 방식으로 다시 고안해보았다.

### 🚩Try 2 (final)

**이전에 나열했던 dp[]**

| index | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| 최대 돈 가치 | nums[0] = 2 | nums[1] = 7 | 11 | 11 | 12 |

→ **i=2부터 시작, max( dp[i-1], nums[i] +dp[i-2] )**

1. **dp[0] = nums[0] = 2**
2. **dp[1] = nums[1] = 7**
3. **dp[2] =max(7, 9+2) = max(7,11) = 11**
4. **dp[3] = max(11, 3+7) = max(11, 10) = 11**
5. **dp[4] = max(11, 1+11) = max(11,12) = 12**

**수정한 dp[]**

| index | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| 최대 돈 가치 | 0 | nums[0] = 2 | 7+0=7 | 11 | 11 | 12 |

→ **i=2부터 시작, max( dp[i-1], nums[i-1] +dp[i-2] )**

1. **dp[0] = 0**
2. **dp[1] = nums[0] = 2**
3. **dp[2] =max(2, 7+0) = max(7,0) = 7**
4. **dp[3] = max(7, 9+2) = max(7, 11) = 11**
5. **dp[4] =max(11, 3+7) = max(11, 10) = 11**
6. **dp[5] = max(11, 1+11) = max(11,12) = 12**

수정한 리스트를 참고하여 다시 재코딩하였다.

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        
        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
            
        return dp[-1]
```

1. `dp` 리스트 초기화, `nums`의 length에 +1을 해주는 이유는 `dp[0]`의 값은 0을 넣어주기 때문에 `nums`의 값들이다 들어오려면 length+1이 되어야 한다.
2. `dp`에는 `nums`에 해당하는 최대 가치가 저장된다. 
3. `dp[1]`에는 `nums[0]`의 값을 넣어준다.
4. dp에 1까지 찼으니까 index 2부터 시작한다.
5. 직전에 있는 값과 `nums[i-1]`과 `dp[i-2]`를 더한 값 중 큰 값을 `dp`리스트에 저장한다. 인접한 인덱스에는 방문하지 못하는 조건이 있기 때문에 `dp[i-2]`로 설정한다.

![여러번 시도 끝에.JPG](#198%20House%20Robber%20ca9def1911c947e6ab5c25bfee250a52/%25EC%2597%25AC%25EB%259F%25AC%25EB%25B2%2588_%25EC%258B%259C%25EB%258F%2584_%25EB%2581%259D%25EC%2597%2590.jpg)

![리절트.JPG](#198%20House%20Robber%20ca9def1911c947e6ab5c25bfee250a52/%25EB%25A6%25AC%25EC%25A0%2588%25ED%258A%25B8.jpg)

여러번의 시도 끝에 성공한 흔적.. 

## Another (different) submission

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(nums))]
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp.pop()
```

![리절트2.JPG](#198%20House%20Robber%20ca9def1911c947e6ab5c25bfee250a52/%25EB%25A6%25AC%25EC%25A0%2588%25ED%258A%25B82.jpg)

- 첫번째 시도 때 index에 0을 주어야 해결된다고 생각했는데, 위 코드처럼 리스트의 길이를 +1 하지 않더라도 예외의 경우를 설정해주면 해결할 수 있다는 것을 알게 되었다.

# 💡Remembrance

- constraints에 주의하자! 예제의 경우만 두고 판단하지 말고 constraints의 최솟값과 최댓값이 들어가도 실행이 잘 될지 살펴보아야 한다.
- 리스트의 맨 마지막 값을 return할 때 (풀이과정의 내용이 stack을 사용하지 않는다고 하더라도) li[-1]로 구현할 수도 있지만 li.pop()을 통해서도 구현할 수 있다는 것을 알게 되었다.
- 보자마자 dp로 접근하고 표를 만들어 점화식을 세우게 되었다. 이전에 dp 공부를 한 게 도움이 되어서 뿌듯했던 문제이다.