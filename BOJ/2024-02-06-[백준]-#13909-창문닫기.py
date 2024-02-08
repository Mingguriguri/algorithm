from sys import stdin
N = int(stdin.readline())
result = 0
cnt = 1
while cnt*cnt <= N:
    cnt += 1
    result +=1
print(result)

# 아래와 같은 방법으로도 풀 수 있음
# # 결국 N에 루트를 씌운 부분의 정수 부분만큼 열려있다.
# print(int(input()**0.5))
