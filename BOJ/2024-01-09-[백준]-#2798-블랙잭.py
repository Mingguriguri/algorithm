# N장의 카드 중 3장의 카드를 골라 그 합이 M을 넘지 않으면서 M과 최대한 가까워야 한다.
# 입력
N, M = map(int, input().split())
num_list = [int(x) for x in input().split()]
answer = 0

# 로직
'''
우선 num_list를 정렬한다.
3장의 카드를 골라야 하므로, 3중 for문을 사용한다.
i는 0~N-2까지, j는 1~N-1까지, k는 2~N까지 반복한다.
i, j, k번째 인덱스에 해당하는 값을 모두 더한 값이 M보다 작거나 같다면, 
지금까지 작은 것 중에서 가장 큰 answer값과 새로 더한 값 중에서 더 큰 값을 answer에 저장한다(max함수 이용)

(M을 넘어서면 안 되지만 뒤에 더 가능성 있는 경우의 수가 있기 때문에 M보다 큰 경우는 고려하지 않고
작은 경우만 고려하여 계산한다.)
'''
num_list.sort()
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if num_list[i] + num_list[j] + num_list[k] <= M:
                print(num_list[i], num_list[j], num_list[k])
                answer = max(answer, num_list[i] + num_list[j] + num_list[k])
                
# 출력
print(answer)
