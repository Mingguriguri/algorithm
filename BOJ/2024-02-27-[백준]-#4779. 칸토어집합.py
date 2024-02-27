import sys
input = sys.stdin.readline

def cut(start, N):
    global cantor
    if N == 1: # N이 1인 경우, 자를 필요가 없기 때문에 바로 return
        return 
    cantor[(start + N // 3) : start + (N // 3 * 2)] = ' ' * (N//3) # 가운데 부분 공백으로 바꾸기
    cut(start, N//3) # 왼쪽 부분 인덱스부터 자르기 시작
    cut(start + (N // 3 * 2), N // 3) # 오른쪽 부분 인덱스부터 자르기 시작

while True:
    try:
        N = int(input())
        cantor = ["-"] * (3**N)
        cut(0, 3 ** N) # 자르기 시작
        print(''.join(cantor))
    except: # 파일의 끝에서 입력을 멈춤
        break