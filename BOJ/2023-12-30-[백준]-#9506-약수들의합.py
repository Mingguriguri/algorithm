# BOJ. #9506-약수들의 합
# n이 완전수라면 n을 n이 아닌 약수들의 합으로 나타내어 출력(오름차순)
# n이 완전수가 아니라면 n is NOT perfect 출력

'''
약수를 구하면서 동시에 완전수를 확인한다.
i값을 증가시키며 나누어 떨어진다면, 배열에도 i의 값을 perfectCheck에도 값을 뺀다.
값이 0이 될 때까지 빼는 것을 반복한다.
이때 값이 음수가 된다면 완전수가 아니다.
값이 0이라면, 배열에 있는 값을 하나씩 출력한다.
'''

### 내 풀이
'''
nums = []
while True:
    n = int(input())
    if (n == -1):
        break
    else:
        nums.append(n)

for number in nums:
    yaksu = 1
    perfectCheck = number - yaksu
    answer = [1]
    while perfectCheck >= 0:
        yaksu += 1
        if (number % yaksu == 0):
            perfectCheck -= yaksu
            answer.append(yaksu)
            if perfectCheck == 0:
                answer.sort()
                break
            if perfectCheck < 0:
                print("%d is NOT perfect"%number)

    if perfectCheck == 0:
        print("%d = 1"%number, end="")
        for i in range(1, len(answer)):
            print(" + %d"%answer[i], end="")
        print("")
'''

### 정답
while True:
    n = int(input())
    if n == -1: # 입력 값이 -1이면 반복문 종료
        break;
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) == n:
        print(n, " = ", " + ".join(str(i) for i in arr), sep="")
    else:
        print(n, "is NOT perfect.")