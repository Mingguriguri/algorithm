from sys import stdin

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True
            
n = int(stdin.readline())
for _ in range(n):
    testCase = int(stdin.readline())
    while True:
        if testCase == 0 or testCase == 1:
            print(2)
            break
        if isPrime(testCase):
            print(testCase)
            break
        else:
            testCase += 1