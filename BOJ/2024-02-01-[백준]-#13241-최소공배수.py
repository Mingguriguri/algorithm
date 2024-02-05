from sys import stdin

def GCD(a, b):
    if a == 0:
        return b
    else:
        return GCD(b%a, a)

a, b = map(int, stdin.readline().strip().split())
   
if(a > b):
    temp = a
    a = b
    b = temp
G = GCD(a,b)
L = G * (a//G) * (b//G)
print(L)
