# #232. Implement Queue using Stacks

progress: Done
review: 🥜
site: LeetCode
등급: Easy
링크: https://leetcode.com/problems/implement-queue-using-stacks/
복습: No
유형: 스택/큐, 자료구조
작성일시: 2022년 12월 28일 오전 10:44
체크박스2: No

# 📖Description

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:

- `void push(int x)` Pushes element x to the back of the queue.
- `int pop()` Removes the element from the front of the queue and returns it.
- `int peek()` Returns the element at the front of the queue.
- `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

**Notes:**

- You must use **only** standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

# 🔍My submission

## 1.  set functions

수가 들어오면 그 수를 저장할 공간이 필요하다.

저장공간이 될 리스트 필요하다.

```python
def __init__(self):
	self.li = [] #리스트선언
```

→ 이렇게 하는 것을 “객체화”라고 한다.

```python
  def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.li.append(x)
```

`push`는 리스트에 추가된 것이기 때문에 list함수의 `append`를 사용하면 된다.

```python
 def pop(self):
        """
        :rtype: int
        """
        return self.li.pop(0) #list의 pop함수
```

pop또한 list의 `pop()`을 사용하면 된다.

```python
    def peek(self):
        """
        :rtype: int
        """
        peeks = self.li[0] #return self.li[0]
        return peeks
```

`peek()`은 pop과는 다르게 가장 첫 부분을 보여주기만 한다. pop처럼 빼지는 않는다.

```python
    def empty(self):
        """
        :rtype: bool
        """
        if len(self.li) == 0:
            return True
        else:
            return False
```

`empty()`description에는 “`boolean empty()` Returns `true` if the queue is empty, `false` otherwise.”라고 나와있다. 이 문장을 그대로 코드로 옮겨주면 된다.

## All code

```python
class MyQueue(object):

    def __init__(self):
        self.li = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.li.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.li.pop(0) #list의 pop함수
        

    def peek(self):
        """
        :rtype: int
        """
        peeks = self.li[0] #return self.li[0]
        return peeks
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.li) == 0:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

# 💡Remember

- 클래스에 저장되어야 하는 특징과 특정함수를 어떻게 동작하게 해야 할지 기억하자!
- stack에 너무 겁먹지 말자.
- `stack`을 이용해 `FIFO`를 구현해보았다.