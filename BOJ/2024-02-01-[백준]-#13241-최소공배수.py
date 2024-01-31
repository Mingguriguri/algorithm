from sys import stdin

def GCM(a, b):
    if a == 0:
        return b
    else:
        return GCM(b%a, a)

a, b = map(int, stdin.readline().strip().split())
   
if(a > b):
    temp = a
    a = b
    b = temp
G = GCM(a,b)
L = G * (a//G) * (b//G)
print(L)
