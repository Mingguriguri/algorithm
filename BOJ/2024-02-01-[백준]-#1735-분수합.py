from sys import stdin

def GCM(a, b):
    if a == 0:
        return b
    else:
        return GCM(b%a, a)

aChild, aParent = map(int, stdin.readline().strip().split())
bChild, bParent = map(int, stdin.readline().strip().split())

if(aParent > bParent):
    temp = aParent
    aParent = bParent
    bParent = temp

G = GCM(aParent,bParent)
aMok = aParent//G
bMok = bParent//G
if aParent == G:
    aMok = 1
if bParent == G:
    bMok = 1
    

ansChild = aChild * aMok + bChild * bMok
ansParent = G * aMok * bMok
print(ansChild, ansParent)
