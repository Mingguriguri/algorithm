#입력
n = int(input())
answer = 666
cnt = 0

# 로직
'''
'666'이 answer에 있을 때마다 카운트(cnt)
cnt가 n과 같아질 때까지 반복하여 answer의 값을 1씩 증가시킴
'''
while n != cnt:
    if '666' in str(answer):
        cnt += 1
        #print(cnt, answer)
        if n==cnt:
            break

    answer += 1
# 출력
print(answer)