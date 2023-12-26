N, b = input().split()
jinsu = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0
N = N[::-1]

for i, n in enumerate(N):
    result += (int(b)**i)*(jinsu.index(n))
print(result)