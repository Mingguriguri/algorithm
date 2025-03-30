import sys
input = sys.stdin.readline

'''
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
중복된 수열은 여러 번 출력되면 안 된다.

왜 이 유형이 백트래킹이지?
순열로 접근해도 되는데.
'''
N, M = map(int, input().split())
nums = list(i for i in range(N+1))  # 수열 리스트
visited = [False] * (N+1)


def backtrack(i, temp):
    print(f"=====i: {i}====")
    visited[i] = True
    print(f"visited 현황: {visited}")

    if len(temp) == M:
        print(f"반환할게~ {temp}")
        return temp

    for j in range(1, N+1):
        print(f"num = {j}")
        if not visited[j]:
            temp.append(j)
            visited[j] = True
            backtrack(j, temp)
            visited[j] = False
            print(f"num {j}에 대한 visited 종료: {visited}")
        else:
            return

for i in range(1, N+1):
    data = backtrack(i, [])
    print(f"data: {data}")
    print("=====")