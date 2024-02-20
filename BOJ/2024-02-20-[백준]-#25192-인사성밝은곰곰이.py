N = int(input())  # 채팅 기록의 수를 입력
cnt = 0  # 곰곰티콘이 사용된 횟수를 저장하는 변수
chatMems = set()  # 현재 채팅방에 있는 사람들을 추적할 집합

for _ in range(N):
    new = input().strip()  # 새로운 채팅 기록을 입력받음
    if new == "ENTER":  # ENTER가 들어오면
        chatMems.clear()  # 현재 채팅방에 있는 사람들의 정보를 초기화
    else:  # 채팅을 입력한 경우,
        if new not in chatMems:  # 해당 사용자가 첫 번째로 채팅하는 경우,(= chatMems집합에 없는 경우)
            cnt += 1  # 곰곰티콘이 사용된 횟수 +1
            chatMems.add(new)  # 해당 사용자를 채팅방에 있는 사람들의 집합에 추가

print(cnt)