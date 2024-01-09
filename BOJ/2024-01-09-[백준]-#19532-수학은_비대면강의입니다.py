# 입력
a, b, c, d, e, f = map(int, input().split()) #정수형으로
ansX = 0
ansY = 0

# 로직
'''
x를 -999~999까지 보고, y도 -999부터 999까지 본다. 
2중 for문을 이용하여 a*x + b*y = c, d*x + e*y = f가 성립되는 x,y를 각각 구한다.
'''
for x in range(-999, 1000, 1):
    for y in range(-999, 1000, 1):
        if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
            ansX = x
            ansY = y
            break
# 출력
print(ansX, ansY)