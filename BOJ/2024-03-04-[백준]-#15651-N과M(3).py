import sys
input = sys.stdin.readline

def backtracking():
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    
    for i in range(1, n+1):
        arr.append(i)
        #print("arr append i", arr, i)
        backtracking()
        arr.pop()
        #print("arr pop", arr)


arr = []
n, m = map(int, input().strip().split())
backtracking()