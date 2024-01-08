f_n, f_c = map(int, input().split())
c = int(input())
n = int(input())

'''
f_n * n + f_c  <= c * n인지 비교 후, 참이면 1을 반환 거짓이면 0을 반환
'''

if (f_n * n) + f_c  <= (c * n) and f_n <= c:
    print(1)
else:
    print(0)