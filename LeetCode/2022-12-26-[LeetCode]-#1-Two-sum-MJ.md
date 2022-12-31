# #1. Two sum

progress: In progress
review: 🥜
site: LeetCode
등급: Easy
링크: https://leetcode.com/problems/two-sum/
복습: No
유형: 브루트 포스(완전탐색)
작성일시: 2022년 12월 26일 오후 12:40
체크박스2: No

# 📖Description

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

**>> 해석**

int형 배열과 목표값이 주어진다. 배열 안에 있는 두 숫자의 합이 target이 되는 인덱스를 출력한다.

이때, 각 값이 정확히 하나의 solution이 있다는 가정하에 input을 집어넣는다. 

답변은 임의의 순서로 반환할 수 있다

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

```

**Example 2:**

```
Input: nums = [3,2,4], target = 6
Output: [1,2]

```

**Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

# 💡Process

## 🚩Try : 1

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        for i in range(nums):
            for j in range(i,nums):
                if nums[i]+nums[i+1] == target:
                    answer.append(i)
                    answer.appned(i+1)
        print(answer)
```

**>> Runtime Error**

TypeError: range() integer end argument expected, got list.
for i in range(nums):
Line 9 in twoSum ([Solution.py](http://solution.py/))
ret = Solution().twoSum(param_1, param_2)
Line 38 in _driver ([Solution.py](http://solution.py/))
_driver()
Line 48 in <module> ([Solution.py](http://solution.py/))

## 🚩 Try : 2

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
   
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer.append(i)
                    answer.append(j)
                    break
                else:
                    continue
        print(answer)
```

**결과 >> Wrong answer**

- Runtime: 31 ms

## 🚩Try : 3

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
  
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

**결과 >> Accepted** 

![results1.JPG](#1%20Two%20sum%207b564c638b52449393f3bd76f9bc38d0/results1.jpg)

![results2.JPG](#1%20Two%20sum%207b564c638b52449393f3bd76f9bc38d0/results2.jpg)

- 내가 푼 방식은 부르트포스 알고리즘이기 때문에 간단하지만 시간복잡도는 $O(n^2)$이다.

# 💡Rememberance

- 부르트포스 알고리즘 말고 해쉬테이블을 이용해서 풀면 더 좋다고 한다. 하지만 나 혼자 푸는 건 부르트포스만 가능한 것 같다…