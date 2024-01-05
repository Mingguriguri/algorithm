n = int(input())
if n%2 == 0:
    print((n-1) * (n//2))
    print(2)
else:
    print(n * (n//2))
    print(2)
'''
cnt = 0

# i 0 1 2 3 4 5
# j 6 5 4 3 2 1
for i in range(n-1):
    print("i", i)
    for j in range(i+1,n):
        print("j", j)
        cnt+=1
        print("%d"%cnt)
'''    