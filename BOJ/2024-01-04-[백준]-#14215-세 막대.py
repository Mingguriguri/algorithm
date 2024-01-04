tri = list(map(int, input().split())) #입력 : 1 2 3 /출력 : [1, 2, 3] 
tri.sort()

if tri[0] + tri[1] > tri[2]:
    print(sum(tri))
else:
    print((tri[0] + tri[1])*2 - 1)