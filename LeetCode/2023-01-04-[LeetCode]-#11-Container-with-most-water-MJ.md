# #11. Container with most water

progress: In progress
review: 🥜
site: LeetCode
upload: No
등급: Medium
링크: https://leetcode.com/problems/container-with-most-water/description/
유형: 구현
작성일시: 2023년 1월 4일 오전 10:05

# 📖Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

**Example 1:**

![https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2:**

```
Input: height = [1,1]
Output: 1
```

# 🔍Approach

**input : height (index마다 height 값들이 있음)**

**output : 최대 물의 양**

- **최대 물의 양은 어떻게 구할까?**

![6D362D1B-AE40-4054-882F-C77CCEFDF58A.jpeg](#11%20Container%20with%20most%20water%2048054615393c4875a9e042a598e45c59/6D362D1B-AE40-4054-882F-C77CCEFDF58A.jpeg)

- 이렇게 위의 그림과 같이 물의 총량은 선 사이의 거리 * 짧은 선 길이이다.

먼저 **`1. brute force`**로 푼 다음, **`2. 코드를 최적화`**하는 식으로 접근해보자!

## **1. brute force**

🚩**Flow**

1. [물의 총량 = 선 사이의 거리 * 짧은 선 길이]로 구하기 때문에 각각의 변수가 필요하다.
2. 물의 총량 = `water`, 선 사이의 거리=`width`, 짧은 선 길이 = `h`로 설정하였다.
3. 선 사이의 거리(`width`)를 구하기 위해 이중 for문을 이용해 `i`는 1부터 `len(height)-1` 까지 돌며, `j`는 j는 `i+1`부터 `len(height)`까지 돌게 된다. i에 대해 j가 i+1부터 끝까지 돌며 선 사이의 거리를 구한다. 구한 값은 `width`에 대입한다.
4. 짧은 선 길이(`h`)는 `height[i]`와 `height[j]`중에서 짧은 길이이므로, `min()`함수를 이용해서 구한다.
5. 구한 `width`와 `h`에 대해 그때그때의 `water`의 최댓값을 저장한다. 이는 `water = max(water, width * h)`로 정의했다.
6. 3-5번까지 이중 for문을 통해 반복 수행한다.

🚩**Brute Force code (First Try)**

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
i=1을 left로, 두고 right를 오른쪽으로 가면서 부피를 구한다.
다 구하면 i=i+1, i=n-1까지 탐색한다.
물의 양은 (right-left) * right 로 구한다.
뒤로 갈 때마다 max()로 더한다.

        '''
        water = 0 # 물 

        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                width = j-i 
                h = min(height[i], height[j]) 
                water = max(water, width * h)
        return water
```

• **Time complexity : $O(N^2)$ ⇒ Time Limit Exceeded**

## 2. **최적화하기**

이전 brute force로 submit하면 시간초과가 뜬다! 

따라서 최적화를 통해 시간복잡도를 줄여야한다.

**🚩최적화**

- 계산량에 영향을 주는 **`파라미터(argument)`**는 무엇인지 생각하고 이에 따라 **어떻게 각 값들에 변화를 줘야할지에 대한 조건**을 생각해야 함
- 이 문제에서는 `for문`이 문제이다! 따라서, 2개의 for문을 쓰지 않고 반복할 수 있도록 고민해보자

→ 결국엔 짧은 선 길이가 관건이다! max값을 비교하는 것이라고 생각했는데 

→ left, right가 서로 더 작으면 index를 옮기면서 비교한다.

**🚩 반복할 조건을 생각해보자**

- `left`가 `right`를 제쳐 넘어가면 안 된다. ***(while의 조건이 되겠다)***
- **최적화한 조건을 생각해보자 (**left, right가 서로 더 작으면 index를 옮기면서 비교)
    - `height[left]`의 값이 작으면 `left+=1`
    - `height[right]`의 값이 작으면 `right-=1`
    

🚩**Flow**

1. `left`와 `right`는 인덱스를 의미한다. `left`는 왼쪽에서 오는 인덱스, `right`는 오른쪽에서 오는 인덱스이다. `left=0`, `right=len(height)-1`(마지막)으로 정의해준다.
`water`는 물의 양을 의미하는 변수로 초기엔 0으로 초기화해준다.
2. **[물의 총량 = 선 사이의 거리 * 짧은 선 길이]**로 구하기 때문에 각각의 변수가 필요하다. 
물의 총량 = `water`, 선 사이의 거리= `width`, 짧은 선 길이 = `h`로 설정하였다.
3. `width`(가로)는 left와 right의 거리차이이다. `right-left`하여 width에 대입한다.
4. `h`(짧은 선 길이)는 `height[left]`와 `height[right]`의 값 중에서 **더 작은 값**이 와야 하므로 `min()`함수를 통해 구해준다.
5. `water`(물의 총량)은 최대 총량을 구해야 한다. 따라서 `max()`함수를 이용해 이전 `water`와 새롭게 `width * h`로 구한 값 중에 더 큰 값을 다시 `water`에 저장한다. (`water = max(water, width*h)`)
6. 구하는 과정에서 `left`와 `right`의 길이가 더 작은 값은 해당 인덱스의 위치를 `left`는 뒤로, `right`는 앞으로 바꾸어줘야 한다.
즉, `height[left]`가 `height[right]`보다 작다면, `left`를 **+1**해주고, 그게 아니라면 `right`를 **-1** 해준다.
7. 위 과정은 4~6번을 `left<right`를 만족할 때까지 **반복**한다.

🚩**Final code**

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0 # 물
        left = 0
        right = len(height)-1
 
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            water = max(water, width * h)
           
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
               
        return water
```

• **Time complexity : $O(N)$**

![result1.JPG](#11%20Container%20with%20most%20water%2048054615393c4875a9e042a598e45c59/result1.jpg)

![results2.JPG](#11%20Container%20with%20most%20water%2048054615393c4875a9e042a598e45c59/results2.jpg)

내가 한 코드가 좀 뒤에 있는 이유가 변수를 추가적으로 만들어서 그런 것 같다.

**extra1) 변수를 줄인 코드**

```python
class Solution(object):
    # @return an integer
    def maxArea(self, height):
        max_area, left, right = 0, 0, len(height) - 1
        while left < right :
            max_area = max(max_area, min(height[left], height[right]) * (right  - left))
            if height[left] < height[right ]:
                left += 1
            else:
                right -= 1
        return max_area
```

**extra2) 선배 코드를 첨부한다.**

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water, water = 0, 0
        start, end = 0, len(height) - 1

        while start != end:
            shorter = min(height[start], height[end])
            water = shorter * (end - start)
            if max_water < water:
                max_water = water

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
                
        return max_water
```

# 💡Recollection ; 회고

- 문제를 어떻게 풀어야 할지 모르겠을 때는 **Brute Force로 먼저 풀기!**
- 이후에 `testcase`가 다 통과했다면, 이를 어떻게 **최적화할 수 있을지에 대해 고민해보기!**
    - 최적화를 하려면 계산량에 영향을 주는 파라미터가 무엇인지 분석해야 함
    - 이후 이 파라미터를 어떻게 대체할 것인지 조건을 고민해보기
- 이전에는 ***flow***를 대충 썼는데 오늘 선배 덕에 ***flow***를 어떻게 써야 하는지 알게 되었다. 정리할 때는  어떻게 적어야할지 머리 속이 뒤죽박죽일 때도 있고, 이렇게까지 자세히 해야 하나 싶을 때도 있었다. 하지만 그렇게 정리하고 나니까 **나중에 다시 볼 때도 쉽게 이해할 수 있고, 마무리하는 과정에 있어서도 잘 정리가 되는 느낌**이다.
    - flow : 1. 변수, 2. 반복하는 내용, 3. 언제까지 반복해야 하는지
- 개인적으로 이 문제를 brute force로 풀고나서 최적화하는 과정에 조건들을 찾는 시간이 좀 새로웠던 것 같다. *이렇게 생각할 수 있구나!!* 하고.