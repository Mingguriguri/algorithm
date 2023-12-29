#n = int(input())
n = 15
idx = 1
count = 0
size=0

while n > count:
    size += 1
    count += size
    print("size", size, "count", count)
    
print("끝")

size+=1
print("최종 size: ", size)
while n > 0: 
    if n - idx <= 0:
        break
    n -= idx
    idx += 1
    print(n, idx)

print("n: ", n)

if size%2 == 0:
    print("%d/%d"%(size-n,n))
else:
    print("%d/%d"%(n,size-n))
