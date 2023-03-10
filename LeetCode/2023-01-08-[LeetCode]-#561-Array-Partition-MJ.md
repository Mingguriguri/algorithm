# [#561. Array Partition](https://leetcode.com/problems/array-partition/)
`LeetCode` - Easy
# ๐Problems

Given an integer arrayย `nums`ย ofย `2n`ย integers, group these integers intoย `n`ย pairsย `(a1, b1), (a2, b2), ..., (an, bn)`ย such that the sum ofย `min(ai, bi)`ย for allย `i`ย isย **maximized**. Returnย *the maximized sum*.

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

# ๐Solution

๋ฌธ์ ๊ฐ ์ ์ดํด๊ฐ ๊ฐ์ง ์๋๋ค. ๋ฌธ์ ๋ฅผ ๋ฒ์ญํด๋ณด์.

- 2n๊ฐ ์ ์์ ์ ์ ๋ฐฐ์ด ๋ฒํธ๊ฐ ์ฃผ์ด์ง๋ฉด**, ๋ชจ๋  i์ ๋ํ ์ต์(ai, bi)์** **ํฉ์ด ์ต๋๊ฐ ๋๋๋ก** ์ด ์ ์๋ค์ n๊ฐ์ ์(a1, b1), (a2, b2), ..., (an, bn)์ผ๋ก ๊ทธ๋ฃนํํฉ๋๋ค. **์ต๋ํ๋ ํฉ๊ณ๋ฅผ ๋ฐํ**ํฉ๋๋ค.

โ ์ฆ, ๊ทธ๋ฃนํํ์ฌ ์ง์ ์ง์ **์๋ค์ min()์ ํฉ์ฐํ์ ๋ ์ต๋**๋ฅผ ๋ง๋๋ ๋ฌธ์ ์ด๋ค. 

์์๋ก ๋ค์ด์จ [1, 4, 3, 2]๋ก ๋ถ์ํด๋ณด์

์ด๋ฅผ ์ ๋ ฌ์ ํ๋ค๋ฉด [1, 2, 3, 4]๊ฐ ๋๋ค. ๊ฐ๊ฐ์ ์์ (1, 4)์ (2, 3), (1, 3)๊ณผ (2, 4), (1, 2)์ (3, 4)๊ฐ ์๋ค.

์ด๋ค์ min()์ผ๋ก ํ ํ ํฉ์ฐํด๋ณด์.

1. min(1, 4) + min(2, 3) = 1 + 2 = 3
2. min(1, 3) + min(2, 4) = 1 + 2 = 3
3. min(1, 2) + min(3, 4) = 1 + 3 = 4

๋ฐ๋ผ์ ์ด๋ค ๊ฐ๋ค ์ค ๊ฐ์ฅ ํฐ ๊ฐ์ 4์ด๋ฏ๋ก 4๊ฐ ์ต๋๊ฐ ๋๋ค. ์ต๋๊ฐ ๋๋ 4๋ ์ค๋ฆ์ฐจ์์ผ๋ก ์ ๋ ฌํ์ ๋ ์ต๋๊ฐ ๋๋ ๊ฒ์ ๋ณผ ์ ์๋ค.

๋ค๋ฅธ ์์ ๋ ๋ง์ฐฌ๊ฐ์ง์ด๋ค.

nums = [6,2,6,5,1,2]์ผ๋์ ๊ฒฝ์ฐ๋ฅผ ๋ณด์. ์ ๋ ฌํ๋ฉด [ 1, 2, 2, 5, 6, 6]์ด๋ฉฐ

min(1, 2) + min(2, 5), min(6, 6) = 1 + 2 + 6 = 9๋ก output๊ณผ ์ผ์นํ๋ค.

์ด๋ฅผ ํ ๋๋ก flow๋ฅผ ์ง๋ณด๊ฒ ๋ค.

- minํจ์๋ฅผ ํตํด ๋ํ ๊ฐ์ ์ ์ฅํ  `sum` ๋ณ์๋ฅผ 0์ผ๋ก ์ด๊ธฐํํ๋ค. ๊ฐ ์์ appendํ  ๋ฆฌ์คํธ `jjak`์ ์ ์ธํด์ค๋ค. ์ดํ, `nums`๋ฅผ ์ค๋ฆ์ฐจ์์ผ๋ก ์ ๋ ฌํ๋ค.
- ์ ๋ ฌํ `nums`์ `i`๋ฒ์งธ๋ถํฐ `jjak`์ appendํ์ฌ ์์ ์ด๋ฃฌ๋ค.
- ์ดํ min๊ฐ์ ๊ตฌํ ๊ฐ์ `sum`์ ์ ์ฅํ๋ค. ๋ค์ `jjak`๋ฆฌ์คํธ๋ฅผ ์ด๊ธฐํํ ํ, ๋ค์ ์์ ๋ง๋ค์ด์ค๋ค.
- ์ ๊ณผ์ ์ `nums`๋ฆฌ์คํธ๊ฐ ๋๋  ๋๊น์ง ๋ฐ๋ณตํ๋ค.
- `sum`์ ๋ฐํํ๋ค.

## ๐ฉMy submission

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
            # ์์์๋ถํฐ ์ค๋ฆ์ฐจ์์ผ๋ก ์ง์ ๋ง๋ค์ด ํฉ ๊ณ์ฐ
            jjak.append(i)
            if len(jjak) == 2:
                sum += min(jjak)
                jjak = []

        return sum
```
![561_solve](https://user-images.githubusercontent.com/101111603/211200432-ea70c7ad-b1c4-4bd6-98e7-695717d17238.jpg)


## ๐ฉOthers submission

1. **์ง์๋ฒ์งธ ๊ฐ ๊ณ์ฐ**
- ์์ ์ง์ ๋ฒ์งธ ๊ฐ๋ถํฐ ์์ํ๋ค. ๋ฐ๋ผ์ min()์ ๊ตฌํ์ง ์๋๋ผ๋ ์ง์ ๋ฒ์งธ ๊ฐ์ ๋ํ๋ฉด ๋๋ค.
- ์ ๋ ฌ๋ ์ํ์์๋ ์ง์๋ฒ์งธ์ ํญ์ ์์ ๊ฐ์ด ์์นํ๋ค.

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
![solve2](https://user-images.githubusercontent.com/101111603/211200411-5de172a3-8761-4f68-9080-bef359b2e546.jpg)


- ์์ด๋์ด๋ฅผ ์๊ฐํด๋ด๋ฉด ํจ์ฌ ๋ ๋จ์ํด์ง๋ ๊ฒ ๊ฐ๋ค.
- ๋ฌธ์ ์์ `min()`์ ์ฐ๋ผ๋ ๋๋์ ๋ฐ์์ ์ด ๋ฐฉ์์ ์๊ฐ ๋ชปํ์ ๊ฒ ๊ฐ๋ค.
- ์ฝ๋๋ ๊ฐ๊ฒฐํ๊ณ  ๋ณด๊ธฐ ์ฝ๋ค. ํ์ง๋ง ๋ฐํ์ ์์ฒด๋ ์์ ๋น์ทํ๋ค.

2. **์ฌ๋ผ์ด์ฑ์ ์ด์ฉํ ํ์ด์ฌ๋ค์ด ๋ฐฉ์**

์ฌ๋ผ์ด์ฑ์ ํ์ฉํ๋ฉด ๋จ ํ ์ค๋ก ํ์ดํ  ์ ์๋ค. ***(Pythonic Way)***

```python
class Solution(object):
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])
```
![solve3](https://user-images.githubusercontent.com/101111603/211200442-e2c6e0fc-2c2f-4b9f-b695-bbf3e8826449.jpg)


- ์ด์  1๋ฒ์ฒ๋ผ ๊ฒฐ๊ตญ์ ์ง์๊ฐ์ ๋ํ๋ ๊ฒ์ด๊ธฐ ๋๋ฌธ์ ์ฌ๋ผ์ด์ฑ์ ํตํด 2์ฉ ๋ํ๋ฉด ๋๋๋ค.

โ ๋ฐํ์์ด๋ ๋ฉ๋ชจ๋ฆฌ๋ 3๋ฐฉ๋ฒ ๋ชจ๋ ํฌ๊ฒ ์ฐจ์ด๊ฐ ์๋ค.

# ๐กRetrospect ํ๊ณ 

- ์ค๋ฆ์ฐจ์์ผ๋ก ๋ง๋ค์ด ํธ๋ ๊ฒ๊น์ง ๋๊ฒ ์ค๋๊ฑธ๋ ธ๋๋ฐ ์กฐ๊ธ ๋ ๊ณ ๋ฏผํ๊ณ  ์กฐ๊ธ ๋ ๋ฌธ์ ์ ํจํด์ ํ์ํ๋ค๋ฉด ๋ ์ฝ๊ฒ ์ฝ๋๋ฅผ ์งค ์ ์๋ค๋ ๊ฒ์ ์๊ฒ ๋์๋ค.

# ๐ฏReference

- ํ์ด์ฌ ์๊ณ ๋ฆฌ์ฆ ์ธํฐ๋ทฐ_ 191p-192p
