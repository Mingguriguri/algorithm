n = int(input())
ans = 0
if n%2 == 0: #짝수일 때
    for i in range((n-2) // 2):
        ans += (i+1) * (n-2-i) * 2
else: #홀수일때
    for i in range(n//2 -1):
        ans += (i+1) * (n-2-i) * 2
    ans+=(n//2) * (n//2)

print(ans)
print(3)
