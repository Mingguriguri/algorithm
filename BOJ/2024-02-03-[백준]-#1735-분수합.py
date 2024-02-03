from sys import stdin

def GCM(a, b):
    if a == 0:
        return b
    else:
        return GCM(b%a, a)

aChild, aParent = map(int, stdin.readline().strip().split())
bChild, bParent = map(int, stdin.readline().strip().split())

ansChild = (aChild * bParent + bChild * aParent) # 분자
ansParent = aParent * bParent  # 분모

G = GCM(ansChild, ansParent)

ansChild = ansChild // G
ansParent = ansParent // G

print(ansChild, ansParent)