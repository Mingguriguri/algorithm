# #20. Valid Parentheses

progress: Done
review: 🥜
site: LeetCode
등급: Easy
링크: https://leetcode.com/problems/valid-parentheses/
복습: No
유형: 스택/큐
작성일시: 2022년 12월 28일 오후 4:54
체크박스2: Yes

# 📖Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**

```
Input: s = "()"
Output: true

```

**Example 2:**

```
Input: s = "()[]{}"
Output: true

```

**Example 3:**

```
Input: s = "(]"
Output: false
```

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
```

# 🔍Process

## First Try

저번에 했던 `()`괄호 짝 맞추는 코드를 가장 먼저 떠올려보았다.

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            (')':'('),
            ('}':'{'),
            (']':'['),
        }
        stack = []
        for i in enumerate(s):
            for b in brackets:
                if i == b[i]:
                    stack.append(i)
                elif i == b[i].values
                    stack.pop()
                else:
                    return False
        
        return True
```

**Result : Runtime Error**

Reason 1 Dictionary Definition 딕셔너리 `brackets`를 잘못 정의함

Reason2.

```python
SyntaxError: invalid syntax
^
elif i == b[i].keys
Line 17  ([Solution.py](http://solution.py/))
```

## Second Try

위의 방식처럼 2중for문을 사용하기 싫어서 다시 방법을 고민해보았다.

1. dictionary로 `( )`, `{ }`, `[ ]` 를 정의
2. `(`, `{`, `[` 처럼 여는 괄호일 때는 다 스택에 저장
3. 맞는 짝이 들어오면 스택에서 pop
4. stack이 없으면 true return, stack이 남아있으면 false return

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for i in enumerate(s):
            if i not in brackets:
                stack.append(i)
            elif len(stack) == 0 or stack.pop() != brackets[i]:
                return False
        return True
```

![result3.JPG](#20%20Valid%20Parentheses%2069a581f4df0b4f8fab14eec521af3854/result3.jpg)

→ 마지막 Testcase만 통과되지 않았다.

`enumerate`를 사용했기 때문에 발생한 것으로 보인다.

## My submission

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for i in s:
            if i not in brackets:
                stack.append(i)
            elif len(stack) == 0 or stack.pop() != brackets[i]:
                return False
        return len(stack) == 0
```

최종 코드는 위와 같다.

1. **여는 괄호가 value, 닫는 괄호가 key**인 dictionary를 만든다.

1. 문자열의 문자를 하나씩 본다. (`for i in s :`)

3. 여는 괄호가 나오면 Stack에 넣는다. 여는 괄호가 values를 저장해두었다. keys값에 없다면 여는 괄호를 의미한다.

4. 닫는 괄호일 경우 stack 최상단에 있는 것과 같은 종류일 경우 stack에서 `pop()`한다.

5. 종류가 다르거나 이미 스택이 비어있다면(빼낼 괄호가 없으므로)  `False`를 return한다.

6. 문자열을 전부 볼 때 까지 2~5를 반복한다.

7. stack이 비어있으면 `True`, 없으면 `False`를 return한다. stack이 비어있다면 짝이 맞았다는 것을 의미하고 stack에 무언가 남아있다면 짝이 맞지 않다는 것을 의미한다.

## Others submission

**메모리가 제일 적은 코드**

```python
class Solution(object):
    pairs = {')': '(',
             '}': '{',
             ']': '['}
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c not in self.pairs:
                stack.append(c)
            else:
                if not stack or stack[-1] != self.pairs[c]:
                    return False
                stack.pop()
        return not stack
```

**Runtime이 가장 적은 코드**

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        
        for p in s:
            if len(s) > 1:
                if p in dict.values():
                    stack.append(p)
                elif stack and dict[p] == stack.pop():
                    continue
                else:
                    return False
            else:
                return False
        
        if stack:
            return False
        else:
            return True
```

**선배 코드**

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(':')', '{':'}', "[":"]"}
        key_dict = list(dict.keys())
        value_dict = list(dict.values())
        stack = []
        for c in s:
            if c in key_dict:
                stack.append(c)
            else:
                if stack and dict[stack[-1]] == c:
                    stack.pop(-1)
                else:
                    return False
        if stack:
            return False
        else:
            return True
```

# 💡Remembrance

- 짝을 맞추는 문제에서는 `stack`을 사용하는 게 더 효율적이다.
- 지난 문제에서 stack을 활용한 괄호문제를 풀었기 때문에 조금 더 수월했고, stack에 대한 복습과 이해도 저번보다 더 잘 되었다. 역시 반복학습이 중요해!
- 여러 사람들의 코드를 보니 코드 구성이 대부분 비슷하였으나, 이해하기 쉬운 코드로 짜는게 가장 좋은 것 같다. 그런 의미로 선배의 코드를 보고 반성했다. 메모리나 런타임이 가장 적게 나오는 코드보다 선배 코드를 이해하는 게 더 쉬웠던 것 같다. 배워간다!