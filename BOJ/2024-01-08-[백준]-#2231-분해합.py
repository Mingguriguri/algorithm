n = int(input())
answer = 0

for i in range(n):
    temp = list(map(int, str(i)))
    answer = i + sum(temp)
    if answer == n:
        answer = i
        break
    elif answer > n:
        answer = 0

print(answer)

########## better code ########## 
# N = int(input())
# x = 0
# for i in range(N):
#     a = list(map(int, str(i)))
#     if N == sum(a) + i:
#         x = i
#         break;
# print(x)