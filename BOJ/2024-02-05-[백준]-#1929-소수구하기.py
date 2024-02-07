import sys

# n보다 작거나 같은 소수들의 리스트를 반환하는 함수
def get_primes(n):
    # 0과 1은 소수가 아니므로 False로 초기화
    is_prime = [False, False] + [True] * (n-1)
    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
            # i의 배수들을 모두 소수가 아닌 것으로 표시
            for j in range(i*2, n+1, i):
                is_prime[j] = False
    return primes

# 입력받은 두 수의 범위를 저장
m, n = map(int, sys.stdin.readline().split())

# n보다 작거나 같은 소수들의 리스트를 구함
primes = get_primes(n)

# m부터 n까지의 수 중에서 소수인 수를 출력
for p in primes:
    if p >= m:
        print(p)