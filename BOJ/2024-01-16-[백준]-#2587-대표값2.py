nums=[]
for _ in range(5):
    nums.append(int(input()))
mean = 0
medianIdx = 2
nums.sort()

for number in nums:
    mean += number
mean //= 5

print(mean)
print(nums[medianIdx])