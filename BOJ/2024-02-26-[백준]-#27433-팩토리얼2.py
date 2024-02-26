import sys2
input = sys.stdin.readline

def factorical(answer, N):
    if N == 0:
        return answer
    else:
        return factorical(answer*N, N-1)


N = int(input())
print(factorical(1, N))
