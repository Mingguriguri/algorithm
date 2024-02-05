from sys import stdin

def GCD(a, b):
    if a == 0:
        return b
    else:
        return GCD(b%a, a)
def ArrGCD(arr):
    gcd = arr[0]
    for item in arr:
        gcd = GCD(gcd, item)
    return gcd
n = int(stdin.readline())       # n: 가로수의 수
front = int(stdin.readline())   # front: 첫번째 가로수의 위치
distance = []                   # distance: 가로수 간의 거리 리스트
cnt = 0                         # cnt: 새로 심어야 하는 수
# 가로수 간의 거리를 distance 리스트에 저장
for i in range(n-1):
    d = int(stdin.readline())
    distance.append(d - front)
    front = d # 앞에 있는 가로수 위치 업데이트
print(distance)

# 거리를 GCD를 이용해 최소 거리를 구하기
resultGCD = ArrGCD(distance)
print("resultGCD", resultGCD)

# GCD 만큼 돌면서 해당 나무가 없으면 심기. 즉 카운트하기
# 이때 거리값에 GCD값을 제외하고 제외한 값에 GCD로 나누었을 때의 몫 값을 이용
for i in range(len(distance)):
    cnt += (distance[i]-resultGCD) // resultGCD
    print(cnt)