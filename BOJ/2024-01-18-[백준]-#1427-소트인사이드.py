N = input()
li = []
for i in range(len(N)):
    li.append(N[i])

li.sort(reverse=True)
print("".join(li))