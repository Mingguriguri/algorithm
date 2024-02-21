N = int(input())    # 사람들이 만난 기록의 수 
rainbow = set()     # 무지개 춤을 추는 사람 집합
rainbow.add("ChongChong")   # 맨 처음에는 ChongChong이만 추기 때문에 ChongChong추가

for _ in range(N):  # N만큼 명령 반복
    A, B = map(str, input().strip().split())  # 만난ㄴ 사람들 A, B
    if A in rainbow or B in rainbow: # A나 B 둘 중 하나라도 rainbow 집합에 있다면 추가
        rainbow.add(A)
        rainbow.add(B)
print(len(rainbow)) # rainbow 집합의 길이 출력