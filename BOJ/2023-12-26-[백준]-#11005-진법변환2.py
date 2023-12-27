num, b =  map(int, input().split())
jinsu = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = []

while num != 0:
    answer.append(jinsu[num%b])
    num = int(num/b)

answer.reverse()
answer = ''.join(answer) 
print(answer)