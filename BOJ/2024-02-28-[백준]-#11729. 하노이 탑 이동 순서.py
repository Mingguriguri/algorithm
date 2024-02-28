def hanoi(N, start, end, sub):
    if N == 1: # 종료조건.
        print(start, end)
        return
   
    hanoi(N-1, start, sub, end) # 1단계
    print(start, end) # 2단계(출력)
    hanoi(N-1, sub, end, start) #3단계

N = int(input())
print(2**N - 1) # 하노이탑 최소 이동 횟수 공식
hanoi(N, 1, 3, 2)
