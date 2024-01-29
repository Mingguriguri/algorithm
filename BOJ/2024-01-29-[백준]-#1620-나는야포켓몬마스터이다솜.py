from sys import stdin
N,M = map(int, stdin.readline().strip().split())
pokemon = {}

# N: 도감에 있는 포켓몬 개수
# M: 내가 맞춰야 하는 문제 개수
# N개의 줄에 
# 포켓몬의 번호가 1번인 포켓몬부터 
# N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력
# 그 다음부터는 내가 맞춰야 하는 게 들어감
######################3

# 초반에 N만큼 반복문을 돌면서 딕셔너리에 저장한다
# 그 후 M만큼 입력받고, 
# 입력받은 수가 숫자면 해당값의 key를, 문자면 value를 출력한다.

for i in range(1, N+1):
    pokemon[stdin.readline().strip()] = i
reverse_pokemon = dict(map(reversed, pokemon.items()))

for i in range(M):
    question = stdin.readline().strip()
    if question.isalpha():
        print(pokemon[question])
    else:
        print(reverse_pokemon[int(question)])