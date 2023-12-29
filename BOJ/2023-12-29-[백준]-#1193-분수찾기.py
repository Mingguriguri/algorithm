n = int(input())
idx = 1
count = 0
size=0

while n > count:
    size += 1
    count += size

size+=1
while n > 0: 
    if n - idx <= 0:
        break
    n -= idx
    idx += 1

if size%2 == 0:
    print("%d/%d"%(size-n,n))
else:
    print("%d/%d"%(n,size-n))
