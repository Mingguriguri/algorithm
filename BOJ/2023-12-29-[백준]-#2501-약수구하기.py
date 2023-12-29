# BOJ. #2501-약수 구하기
# N과 K가 주어졌을 때 N의 약수들 중 K번째로 작은 수 출력
n, k = map(int, input().split())
cnt = 0 # 약수 개수
'''
i가 n일 때까지 i를 1씩 증가시키면서
n과 나누어 떨어지는지 비교해야 한다. 
나누어 떨어질 때마다 count한다(cnt+=1)
이때 count와 k의 값이 같다면 바로 종료하고 값을 반환한다.
'''
for i in range(1, n+1):
    if n % i == 0:
        cnt+=1
        if cnt == k:
            answer = i

if cnt < k:
    print(0)
else:
    print(answer)