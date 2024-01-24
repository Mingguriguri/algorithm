from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().strip().split()))
cnt = list(set(nums))
cnt.sort()
ans ={}

for i in range(len(cnt)):
    ans[cnt[i]] = i
for i in nums:
    print(ans[i], end=' ')