# 입력
n = int(input())
nums = map(int, input().split())

'''
에라토스테네스의 체와 같이 어떤 방법이 있었던 걸로 기억하는데
기억나지 않는다...
주먹구구로 가보자
'''
cnt = 0
for num in nums:
    flag = 1
    if num > 1:
        for j in range(2, num):
            if num % j == 0:
                flag = 0
                break
        if flag == 1:
            cnt += 1

print(cnt)

