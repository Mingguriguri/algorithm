#n = int(input())
n = 1
idx = 1
count = 0
size=0

### size 구하기 ###
print("n: ", n)
while n > count:
    size += 1  # 1 2 3 4 5 ... 순으로 늘리기 위해 1씩 증가
    count += size # size 값을 더해가면서 n이 count보다 작아지는 순간을 구하기
    print("size", size, "count", count)
    
print("size 찾기 끝")

size+=1
print("----최종 size: ", size, "----")

### 분모분자에 들어갈 n값 구하기 ###
print("---- n 구하기 ----")
while n > 0: # n에 idx를 빼면서 구하는 것이므로 0이상인 경우만 반복
    if n - idx <= 0: # 만약 0이하로 떨어지게 되면 반복 중단
        break
    n -= idx # 1 2 3 4 5 ... 씩 빼기
    idx += 1 # idx값 증가 
    print("n", n, "idx", idx)

print("최종 n:", n)  # 0이하가 되기 전의 n의 최종 값

# size가 짤수냐 홀수냐에 따라 분수 
print("======분수 찾기=====")
if size%2 == 0:
    print("%d/%d"%(size-n,n))
else:
    print("%d/%d"%(n,size-n))
