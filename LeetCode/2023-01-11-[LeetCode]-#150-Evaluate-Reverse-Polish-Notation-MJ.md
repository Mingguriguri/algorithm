# **[150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)**
LeetCode - Medium

# 📖Problems

You are given an array of strings `tokens` that represents an arithmetic expression in a [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

Evaluate the expression. Return *an integer that represents the value of the expression*.

**Note** that:

- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
- Each operand may be an integer or another expression.
- The division between two integers always **truncates toward zero**.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a **32-bit** integer.

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

# 🔍Institution

어떤 유형일까? **스택**

- 연산자를 만났을 때 숫자들을 pop해서 해당 연산을 수행하기 때문이다.
- 즉 순서대로 하는 것이 아니라 연산자는 들어온 순서대로 연산자가 들어가고, 숫자는 연산자가 들어올 때 해당 연산이 수행된다. 이는 연산을 만나면 가장 마지막 숫자와 그 앞에 있는 숫자로 연산을 하기 때문에 *LIFO* 형식인 스택이 가장 먼저 생각이 났다.
- **연산자가 피연산자 뒤에 온다!(순서가 입력과 반대이다.)**
    - **[Reverse Polish notation](https://ko.wikipedia.org/wiki/%EC%97%AD%ED%8F%B4%EB%9E%80%EB%93%9C_%ED%91%9C%EA%B8%B0%EB%B2%95) : stack 지향 프로그래밍 언어에 사용되는 표기법**

# 🔍Approach

## 🚩**FLOW**

**tokens = [“2”, “1”, “+”, “3”, “*”] / 연산을 할 숫자 2개가 꼭 있어야 한다.**

1. `stack`을 사용해야 하기 때문에 `stack`리스트를 선언한다. 또한 연산을 수행한 값을 저장하기 위한 변수 `answer`는 0으로 초기화해준다.

2. “`+`”, “`-`”, “`*`”, “`/`” 인 경우

- 스택이 안에 있는지 찾아본다.
- 만약 없다면 다음 인덱스로 넘어간다
- 있다면 `stack[-1]`과 `stack[-2]`를 꺼내 해당 연산을 수행하고 `answer`에 저장한다. (stack.pop()과 stack.pop())
    - 연산 수행 시 주의해야 할 점은 `-` 연산과 `/`연산의 경우, **앞 뒤의 순서**가 중요하다. `stack`을 `pop`할 때 뒤에서 2번째부터 `pop`할 수 있도록 한다.
    - ex) 3-7 = -4, 7-3 = 4, 3/7 = 0, 7/3 = 2

3. 아닌 경우에는 숫자이기 때문에 `stack`에 int형으로 형변환 후, `append`한다.

4. `stack`의 마지막 값을 `return`한다.

## 🚩My submission

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
                # 숫자인 경우이기 때문에 stack에 append한다.
                stack.append(int(tokens[i]))
        return stack.pop()
```

- 시간복잡도 : O(N), 공간복잡도 : O(N)

**헤매었던 부분들**

1. **Wrong Answer**
    - `stack.pop(-2) // stack.pop()` 으로 해서 testcase3가 통과가 되지 않았음.
    - `int(stack.pop(-2) / stack.pop))`으로 바꿨더니 해결됨
2. **submit 제출 시 통과가 되지 않았음**
    - 원인 : tokens = [“18”] 처럼 하나만 들어올 경우 answer는 18이 나와야 하는데 0이 나온다. 이는 마지막에 return answer를 했기 때문이다.
    - 최종답은 answer와 stack에 하나 남은 값과 같기 때문에,
        
        ex) tokens = ["2","1","+","3","*"]
        
        0 [2]
        
        0 [2, 1]
        
        3 [3]
        
        3 [3, 3]
        
        9 [9]
        
        마지막에 return할 때 stack에 맨 마지막 값으로 return하면 된다. (`return stack.pop()`)
        

## 🚩Others submission

다른 이의 코드가 더 깔끔하고 보기 좋아서 가져왔다.

- 먼저 토큰 안에 연산자가 있는지 확인을 한 후에 연산자를 구분한다.
- 또한, pop()하는 것을 변수를 따로 두어 계산하였다. 반복되는 연산이기에 변수를 두는 것이 더 좋았을 것 같다.
- 난 임의로 answer라는 변수를 사용했지만 여기선 변수 사용없이 바로 stack에 append했다. 이렇게 보니 answer의 변수는 굳이 필요하지 않을 것 같다.

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

- 시간복잡도 : O(N), 공간복잡도 : O(N)

# 💡Retrospect

- 스택 문제를 반복해서 풀어보니까 문제만 봐도 어떤 유형인지, 어떤 식으로 구성하면 될 지 감이 왔다. 정말 신기하다. 다른 유형들도 이렇게 반복학습해서 스택처럼 정복해버려야겠다.
- 스택의 경우는 코드를 짠 후 직접 스택에 넣고 빼면서 무엇이 문제인지 찾는 것이 도움이 되는 것 같다.
- 코드를 조금 더 이쁘게 짜는 법을 알게 되었다. 남의 코드를 다 따라할 필요는 없지만 때론 도움이 되는 것 같다. 코드 구성은 같더라도 보기 좋은 코드가 있고 ‘외계인 코드’가 있다. 아직 외계인에서 잘 벗어나지 못한 것 같다. 코드를 다 쓰고 나면 필요없어 보이는 변수는 지우고 반복되는 것이 있다면 변수화를 하며 정리한다. 반복되는 조건이 있다면 한번에 묶어서 큰 틀에 넣어준다.
