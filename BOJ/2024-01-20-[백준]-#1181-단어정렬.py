from sys import stdin
n = int(stdin.readline())
s_list = [input() for _ in range(n)] #예시로 n에 3넣어 3줄 입력받기(엔터로 구분)

# 리스트 내 중복 제거
s_list = list(set(s_list))

# 리스트 정렬
s_list.sort(key=lambda x:(len(x), x))

for s in s_list:
    print(s)