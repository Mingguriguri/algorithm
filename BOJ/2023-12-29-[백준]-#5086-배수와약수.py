nums = []
while True:
    nums.append(list(map(int, input().split())))
    if nums[-1][0] == 0 and nums[-1][1] == 0:
        break
print(nums)

for i in range(len(nums)-1):
    if nums[i][0] < nums[i][1]: # 약수 가능성
        if nums[i][1] % nums[i][0] == 0:
            print("factor") 
        else:
            print("neither")
    elif nums[i][0] > nums[i][1]: # 배수 가능성
        if nums[i][0] % nums[i][1] == 0:
            print("multiple")
        else:
            print("neither")
    else:
        print("neither")