def solution(n):
    a = 0
    b = 1
    temp = 0
    #  0 1 1 2 3 5 8 13 21 34 55
    for i in range(n):
        temp = b
        b = a + b
        a = temp    
        
    return a % 1234567