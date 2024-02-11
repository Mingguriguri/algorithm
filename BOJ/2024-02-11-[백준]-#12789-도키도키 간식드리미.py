from sys import stdin
N = int(stdin.readline()) # 학생들의 수
students = list(map(int, stdin.readline().strip().split())) # 번호 
stack = []

order = 1
while students:
	# students는 FIFO이므로 앞(0)에서부터 처리한다.
	# 만약 order값과 같지 않다면 students에서 제거(pop)하고 stack으로 이동해야 한다.
    if students[0] != order:
        stack.append(students.pop(0)) 
    else: #만약 같다면, order값을 1 증가시키고, students에서도 제거한다.
        order += 1
        students.pop(0)

		# stack에 값이 있다면, stack에서도 다음 순서로 갈 번호가 있는지 확인해야 하므로 while 반복한다.
    while stack:
        if stack[-1] == order: #stack의 마지막 값(-1)이 order와 같다면 stack에서 제거(pop)하고 order+=1
            stack.pop()
            order += 1
        else: #만약 같지 않다면 students를 더 봐야 하는 것이므로 stack에 대한 while반복에서 빠져나온다.(break)
            break
# 마지막에는 stack에 값이 없어야 승환이가 간식을 먹을 수 있다. 따라서 stack에 값이 없다면⇒ “Nice”, 있다면 ⇒ “Sad”를 출력하도록 한다.
if not stack:
    print("Nice")
else:
    print("Sad")