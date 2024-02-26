import sys
input = sys.stdin.readline

# 입력 및 변수 초기화
N, M, B = map(int, input().strip().split())
blocks = [list(map(int, input().split())) for _ in range(N)]
time = sys.maxsize
# 블록 로직
for floor in range(257):
    exceedBlock = 0
    lackBlock = 0

    for i in range(N): # 행
        for j in range(M): # 열
            if floor <= blocks[i][j]:
                exceedBlock += blocks[i][j] - floor
            else:
                lackBlock += floor - blocks[i][j]
    
    if exceedBlock + B >= lackBlock:
        if (exceedBlock * 2) + lackBlock <= time:
            time = (exceedBlock * 2) + lackBlock 
            height = floor

# 출력
print(time, height)