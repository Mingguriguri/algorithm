import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, distance):
    queue = []
    heapq.heappush(queue, (0, start)) # 힙에 (가중치, 노드)형식으로 삽입

    # 현재 출발점과 가장 가깝고, 방문 안한 노드(경유지 찾기)
    while queue:
        dist, now = heapq.heappop(queue)


    return



N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [[ float("inf") for _ in range(N+1)] for _ in range(N+1)] # 최단거리 테이블

for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))
print(graph)

'''
N: 학생 수. 마을 번호 범위.
X: 모이는 마을 번호
M: 마을 사이의 단방향 도로 개수
- i번째 길일 경우 Ti 시간이 걸림

각 경로별로 총 걸리는 시간을 구해야 한다. 이걸 구할 때에는 최소가 되는 걸 구해야 한다.
최소가 되는 값들을 구하고, 그 값들 중에서 최댓값을 구해야 한다. 
어쩄든 T가 가중치 늒ㅁ. 


-- 
왕복의 최단거리를 구해야 함
'''

