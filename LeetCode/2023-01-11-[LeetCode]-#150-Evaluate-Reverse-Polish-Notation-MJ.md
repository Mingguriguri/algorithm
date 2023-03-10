# **[150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)**
LeetCode - Medium

# ๐Problems

You are given an array of stringsย `tokens`ย that represents an arithmetic expression in aย [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

Evaluate the expression. Returnย *an integer that represents the value of the expression*.

**Note**ย that:

- The valid operators areย `'+'`,ย `'-'`,ย `'*'`, andย `'/'`.
- Each operand may be an integer or another expression.
- The division between two integers alwaysย **truncates toward zero**.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in aย **32-bit**ย integer.

**Example 1:**

```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

```

**Example 2:**

```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

```

**Example 3:**

```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

# ๐Institution

์ด๋ค ์ ํ์ผ๊น? **์คํ**

- ์ฐ์ฐ์๋ฅผ ๋ง๋ฌ์ ๋ ์ซ์๋ค์ popํด์ ํด๋น ์ฐ์ฐ์ ์ํํ๊ธฐ ๋๋ฌธ์ด๋ค.
- ์ฆ ์์๋๋ก ํ๋ ๊ฒ์ด ์๋๋ผ ์ฐ์ฐ์๋ ๋ค์ด์จ ์์๋๋ก ์ฐ์ฐ์๊ฐ ๋ค์ด๊ฐ๊ณ , ์ซ์๋ ์ฐ์ฐ์๊ฐ ๋ค์ด์ฌ ๋ ํด๋น ์ฐ์ฐ์ด ์ํ๋๋ค. ์ด๋ ์ฐ์ฐ์ ๋ง๋๋ฉด ๊ฐ์ฅ ๋ง์ง๋ง ์ซ์์ ๊ทธ ์์ ์๋ ์ซ์๋ก ์ฐ์ฐ์ ํ๊ธฐ ๋๋ฌธ์ *LIFO* ํ์์ธ ์คํ์ด ๊ฐ์ฅ ๋จผ์  ์๊ฐ์ด ๋ฌ๋ค.
- **์ฐ์ฐ์๊ฐ ํผ์ฐ์ฐ์ ๋ค์ ์จ๋ค!(์์๊ฐ ์๋ ฅ๊ณผ ๋ฐ๋์ด๋ค.)**
    - **[Reverse Polish notation](https://ko.wikipedia.org/wiki/%EC%97%AD%ED%8F%B4%EB%9E%80%EB%93%9C_%ED%91%9C%EA%B8%B0%EB%B2%95) : stack ์งํฅ ํ๋ก๊ทธ๋๋ฐ ์ธ์ด์ ์ฌ์ฉ๋๋ ํ๊ธฐ๋ฒ**

# ๐Approach

## ๐ฉ**FLOW**

**tokens = [โ2โ, โ1โ, โ+โ, โ3โ, โ*โ] / ์ฐ์ฐ์ ํ  ์ซ์ 2๊ฐ๊ฐ ๊ผญ ์์ด์ผ ํ๋ค.**

1. `stack`์ ์ฌ์ฉํด์ผ ํ๊ธฐ ๋๋ฌธ์ `stack`๋ฆฌ์คํธ๋ฅผ ์ ์ธํ๋ค. ๋ํ ์ฐ์ฐ์ ์ํํ ๊ฐ์ ์ ์ฅํ๊ธฐ ์ํ ๋ณ์ `answer`๋ 0์ผ๋ก ์ด๊ธฐํํด์ค๋ค.

2. โ`+`โ, โ`-`โ, โ`*`โ, โ`/`โ ์ธ ๊ฒฝ์ฐ

- ์คํ์ด ์์ ์๋์ง ์ฐพ์๋ณธ๋ค.
- ๋ง์ฝ ์๋ค๋ฉด ๋ค์ ์ธ๋ฑ์ค๋ก ๋์ด๊ฐ๋ค
- ์๋ค๋ฉด `stack[-1]`๊ณผ `stack[-2]`๋ฅผ ๊บผ๋ด ํด๋น ์ฐ์ฐ์ ์ํํ๊ณ  `answer`์ ์ ์ฅํ๋ค. (stack.pop()๊ณผ stack.pop())
    - ์ฐ์ฐ ์ํ ์ ์ฃผ์ํด์ผ ํ  ์ ์ `-` ์ฐ์ฐ๊ณผ `/`์ฐ์ฐ์ ๊ฒฝ์ฐ, **์ ๋ค์ ์์**๊ฐ ์ค์ํ๋ค. `stack`์ `pop`ํ  ๋ ๋ค์์ 2๋ฒ์งธ๋ถํฐ `pop`ํ  ์ ์๋๋ก ํ๋ค.
    - ex) 3-7 = -4, 7-3 = 4, 3/7 = 0, 7/3 = 2

3. ์๋ ๊ฒฝ์ฐ์๋ ์ซ์์ด๊ธฐ ๋๋ฌธ์ `stack`์ intํ์ผ๋ก ํ๋ณํ ํ, `append`ํ๋ค.

4. `stack`์ ๋ง์ง๋ง ๊ฐ์ `return`ํ๋ค.

## ๐ฉMy submission

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        answer = 0

        for i in range(len(tokens)):
            if tokens[i] == "+":
                if stack:
                    answer = stack.pop() + stack.pop()
                    stack.append(answer)
            elif tokens[i] == "-":
                if len(stack) >= 2:
                    answer = stack.pop(-2) - stack.pop()
                    stack.append(answer)
            elif tokens[i] == "*":
                if len(stack) >= 2:
                    answer = stack.pop() * stack.pop()
                    stack.append(answer)
            elif tokens[i] == "/":
                if len(stack) >= 2:
                    answer = int(stack.pop(-2) / stack.pop())
                    stack.append(answer)
            else:
                # ์ซ์์ธ ๊ฒฝ์ฐ์ด๊ธฐ ๋๋ฌธ์ stack์ appendํ๋ค.
                stack.append(int(tokens[i]))
        return stack.pop()
```

- ์๊ฐ๋ณต์ก๋ : O(N), ๊ณต๊ฐ๋ณต์ก๋ : O(N)

**ํค๋งค์๋ ๋ถ๋ถ๋ค**

1. **Wrong Answer**
    - `stack.pop(-2) // stack.pop()` ์ผ๋ก ํด์ testcase3๊ฐ ํต๊ณผ๊ฐ ๋์ง ์์์.
    - `int(stack.pop(-2) / stack.pop))`์ผ๋ก ๋ฐ๊ฟจ๋๋ ํด๊ฒฐ๋จ
2. **submit ์ ์ถ ์ ํต๊ณผ๊ฐ ๋์ง ์์์**
    - ์์ธ : tokens = [โ18โ] ์ฒ๋ผ ํ๋๋ง ๋ค์ด์ฌ ๊ฒฝ์ฐ answer๋ 18์ด ๋์์ผ ํ๋๋ฐ 0์ด ๋์จ๋ค. ์ด๋ ๋ง์ง๋ง์ return answer๋ฅผ ํ๊ธฐ ๋๋ฌธ์ด๋ค.
    - ์ต์ข๋ต์ answer์ stack์ ํ๋ ๋จ์ ๊ฐ๊ณผ ๊ฐ๊ธฐ ๋๋ฌธ์,
        
        ex) tokens = ["2","1","+","3","*"]
        
        0 [2]
        
        0 [2, 1]
        
        3 [3]
        
        3 [3, 3]
        
        9 [9]
        
        ๋ง์ง๋ง์ returnํ  ๋ stack์ ๋งจ ๋ง์ง๋ง ๊ฐ์ผ๋ก returnํ๋ฉด ๋๋ค. (`return stack.pop()`)
        

## ๐ฉOthers submission

๋ค๋ฅธ ์ด์ ์ฝ๋๊ฐ ๋ ๊น๋ํ๊ณ  ๋ณด๊ธฐ ์ข์์ ๊ฐ์ ธ์๋ค.

- ๋จผ์  ํ ํฐ ์์ ์ฐ์ฐ์๊ฐ ์๋์ง ํ์ธ์ ํ ํ์ ์ฐ์ฐ์๋ฅผ ๊ตฌ๋ถํ๋ค.
- ๋ํ, pop()ํ๋ ๊ฒ์ ๋ณ์๋ฅผ ๋ฐ๋ก ๋์ด ๊ณ์ฐํ์๋ค. ๋ฐ๋ณต๋๋ ์ฐ์ฐ์ด๊ธฐ์ ๋ณ์๋ฅผ ๋๋ ๊ฒ์ด ๋ ์ข์์ ๊ฒ ๊ฐ๋ค.
- ๋ ์์๋ก answer๋ผ๋ ๋ณ์๋ฅผ ์ฌ์ฉํ์ง๋ง ์ฌ๊ธฐ์  ๋ณ์ ์ฌ์ฉ์์ด ๋ฐ๋ก stack์ appendํ๋ค. ์ด๋ ๊ฒ ๋ณด๋ answer์ ๋ณ์๋ ๊ตณ์ด ํ์ํ์ง ์์ ๊ฒ ๊ฐ๋ค.

```python
class Solution(object):
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                # if integer
                stack.append(int(token))

            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    stack.append(num2 + num1)
                elif token == '-':
                    stack.append(num2 - num1)
                elif token == '*':
                    stack.append(num2 * num1)
                elif token == '/':
                    # Beware of rounding
                    stack.append(int(num2 * 1.0 / num1))

        return stack[-1]
```

- ์๊ฐ๋ณต์ก๋ : O(N), ๊ณต๊ฐ๋ณต์ก๋ : O(N)

# ๐กRetrospect

- ์คํ ๋ฌธ์ ๋ฅผ ๋ฐ๋ณตํด์ ํ์ด๋ณด๋๊น ๋ฌธ์ ๋ง ๋ด๋ ์ด๋ค ์ ํ์ธ์ง, ์ด๋ค ์์ผ๋ก ๊ตฌ์ฑํ๋ฉด ๋  ์ง ๊ฐ์ด ์๋ค. ์ ๋ง ์ ๊ธฐํ๋ค. ๋ค๋ฅธ ์ ํ๋ค๋ ์ด๋ ๊ฒ ๋ฐ๋ณตํ์ตํด์ ์คํ์ฒ๋ผ ์ ๋ณตํด๋ฒ๋ ค์ผ๊ฒ ๋ค.
- ์คํ์ ๊ฒฝ์ฐ๋ ์ฝ๋๋ฅผ ์ง  ํ ์ง์  ์คํ์ ๋ฃ๊ณ  ๋นผ๋ฉด์ ๋ฌด์์ด ๋ฌธ์ ์ธ์ง ์ฐพ๋ ๊ฒ์ด ๋์์ด ๋๋ ๊ฒ ๊ฐ๋ค.
- ์ฝ๋๋ฅผ ์กฐ๊ธ ๋ ์ด์๊ฒ ์ง๋ ๋ฒ์ ์๊ฒ ๋์๋ค. ๋จ์ ์ฝ๋๋ฅผ ๋ค ๋ฐ๋ผํ  ํ์๋ ์์ง๋ง ๋๋ก  ๋์์ด ๋๋ ๊ฒ ๊ฐ๋ค. ์ฝ๋ ๊ตฌ์ฑ์ ๊ฐ๋๋ผ๋ ๋ณด๊ธฐ ์ข์ ์ฝ๋๊ฐ ์๊ณ  โ์ธ๊ณ์ธ ์ฝ๋โ๊ฐ ์๋ค. ์์ง ์ธ๊ณ์ธ์์ ์ ๋ฒ์ด๋์ง ๋ชปํ ๊ฒ ๊ฐ๋ค. ์ฝ๋๋ฅผ ๋ค ์ฐ๊ณ  ๋๋ฉด ํ์์์ด ๋ณด์ด๋ ๋ณ์๋ ์ง์ฐ๊ณ  ๋ฐ๋ณต๋๋ ๊ฒ์ด ์๋ค๋ฉด ๋ณ์ํ๋ฅผ ํ๋ฉฐ ์ ๋ฆฌํ๋ค. ๋ฐ๋ณต๋๋ ์กฐ๊ฑด์ด ์๋ค๋ฉด ํ๋ฒ์ ๋ฌถ์ด์ ํฐ ํ์ ๋ฃ์ด์ค๋ค.
