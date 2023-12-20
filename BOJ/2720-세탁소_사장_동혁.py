n = int(input())
test_case = [int(input()) for _ in range(n)]

# c의 단위는 센트 (1달러 = 100센트. 1센트 = 0.01달러)
for cent in test_case:
    # 쿼터 = 센트/25
    # 다임: 센트/10
    # 니켈: 센트/5
    # 페니 : 센트
    quarter = cent/25
    cent %= 25
    
    dime = cent/10
    cent %= 10

    nikel = cent / 5
    cent %= 5

    penny = cent

    print("%d %d %d %d"%(quarter, dime, nikel, cent))