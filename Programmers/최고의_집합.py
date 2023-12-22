def solution(n, s):
    if n>s:
        return [-1]
    multiset = [s//n] * n
    i = n-1
    check = sum(multiset)
    while check != s:
        if check < s:
            multiset[i] += 1
            check += 1
        else:
            multiset[i] -= 1
            check -= 1
        i = (i%n-1)%n
        
                
    return sorted(multiset)