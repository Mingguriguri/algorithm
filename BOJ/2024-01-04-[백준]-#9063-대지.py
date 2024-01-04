n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x_d = max(x) - min(x)
y_d = max(y) - min(y)
print(x_d * y_d)