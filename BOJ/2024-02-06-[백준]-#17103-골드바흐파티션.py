from sys import stdin

# 1. 에라토스테네스의 체 알고리즘으로 일단 소수를 구한다.
# 이때 함수로 구현하지 않고, 미리 주어진 조건인 100,000 크기의 소수 리스트를 미리 만들어 재사용한다.

MAX_N = 1000000
isPrime = [False, False] + [True] * (MAX_N-1)
primes = []
for i in range(2, MAX_N+1):
    if isPrime[i]:
        primes.append(i)
        for j in range(i*2, MAX_N+1, i):
            isPrime[j] = False  

# 2. 입력받기
n = int(stdin.readline())

for _ in range(n):
    testCase = int(stdin.readline())
    # 3. 투 포인터로 같은 값 찾기
    primesList = primes
    count = 0
    left = 0 
    right = len(primesList)-1
    while left <= right:
        if primesList[left] + primesList[right] > testCase:
            right -= 1
        elif primesList[left] + primesList[right] < testCase:
            left += 1 
        else:
            left += 1
            right -= 1
            count += 1
    print(count)