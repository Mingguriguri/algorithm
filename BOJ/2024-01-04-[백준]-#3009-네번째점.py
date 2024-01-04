x = [0]*4
y = [0]*4

for i in range(3):
    a, b = map(int, input().split())
    x[i] = a
    y[i] = b

if x[0] == x[1]:
    x[3] = x[2]
elif x[0] == x[2]:
    x[3] = x[1]
elif x[1] == x[2]:
    x[3] = x[0]

if y[0] == y[1]:
    y[3] = y[2]
elif y[0] == y[2]:
    y[3] = y[1]
elif y[1] == y[2]:
    y[3] = y[0]

print("%d %d"%(x[3],y[3]))