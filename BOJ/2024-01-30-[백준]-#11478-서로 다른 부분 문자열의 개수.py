from sys import stdin
s = stdin.readline().strip()
result = []

for i in range(len(s)):
    for j in range(i, len(s)):
        result.append(s[i:j+1])
print(len(set(result)))