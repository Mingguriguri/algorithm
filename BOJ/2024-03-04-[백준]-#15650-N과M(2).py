import sys
input = sys.stdin.readline

def backtracking(start):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return 
    
    for i in range(start, n+1):
        if i not in arr:
            arr.append(i)
            #print("arr append i", arr, i)
            backtracking(i)
            arr.pop()
            #print("arr pop", i)
    


n, m = map(int, input().strip().split())
arr = []
backtracking(1)