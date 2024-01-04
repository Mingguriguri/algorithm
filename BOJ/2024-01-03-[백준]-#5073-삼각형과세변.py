while True:
    a, b, c = map(int, input().split()) 
    if a == b == c == 0:
        break
    li = [a,b,c]
    if a==b==c:
        print("Equilateral")
    elif a==b or b==c or a==c:
        print("Isosceles")
    elif sum(li) - max(li) <= max(li):
        print("Invalid")
    else:
        print("Scalene")