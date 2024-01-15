n = int(input())
nums = [int(input()) for _ in range(n)] 

nums.sort()
for num in nums:
    print(num)