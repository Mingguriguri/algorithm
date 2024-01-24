from sys import stdin
m = stdin.readline()
nums = list(map(int, stdin.readline().strip().split()))
n = stdin.readline()
cards = list(map(int, stdin.readline().strip().split()))
ans ={}

for i in range(len(cards)):
    ans[cards[i]] = 0
for i in range(len(nums)):
    if nums[i] in ans:
        ans[nums[i]] = 1

for i in ans.values():
    print(i, end=" ")
