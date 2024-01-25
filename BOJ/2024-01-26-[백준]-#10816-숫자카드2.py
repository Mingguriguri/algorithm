from sys import stdin
n = int(stdin.readline())
cards = list(map(int, stdin.readline().strip().split()))
m = int(stdin.readline())
check_list = list(map(int, stdin.readline().strip().split()))

check_dict = {}

# 상근이 카드가 있다면 해당 카드 숫자를 1 증가
for card in cards:
    if card in check_dict:
        check_dict[card] += 1
    else:
        check_dict[card] = 1
    
#{3:2, 2:1,10:3,-10:2}
# 출력
for check in check_list:
    result = check_dict.get(check)
    if result is None:
        print(0, end=' ')
    else:
        print(result, end=' ')
