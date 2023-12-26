n = int(input())

answer = 0
rect = 1
div = 1
for i in range(1, n+1):
    rect *= 4
    div *= 2
    answer = (rect/div+1)**2
print(int(answer))