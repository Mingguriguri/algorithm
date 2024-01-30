from sys import stdin
N,M = map(int, stdin.readline().strip().split())
pokemon = {}

for i in range(1, N+1):
    pokemon[stdin.readline().strip()] = i
reverse_pokemon = dict(map(reversed, pokemon.items()))

for i in range(M):
    question = stdin.readline().strip()
    if question.isalpha():
        print(pokemon[question])
    else:
        print(reverse_pokemon[int(question)])