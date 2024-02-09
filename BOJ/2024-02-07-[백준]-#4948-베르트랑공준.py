from sys import stdin

def getPrime(num):
    isPrime = [False, False]+[True]*(2*num)
    primes = []
    for i in range(2, 2*num + 1):
        if isPrime[i] == True:
            if num < i <= 2*num:
                primes.append(i)
            for j in range(i*2, 2*num+1, i):
                isPrime[j] = False
            
    return primes

while True:
    n = int(stdin.readline())
    if n == 0:
        break
    else:
        #result = getPrime(n)
        print(getPrime(n))
        #print(result)
        print(len(getPrime(n)))