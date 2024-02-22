import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # 단어 개수, 단어 길이
wordsDict= {} # 딕셔너리

for _ in range(N):
    word = input().rstrip()
    
    if len(word) >= M: #단어가 M이상인 경우
        if word in wordsDict: # 단어가 있는 경우 개수 하나 증가
            wordsDict[word][0] += 1
        else: # 단어가 없는 경우 [개수, 길이, 단어] 추가 
            wordsDict[word] = [1, len(word), word]

# 개수, 길이는 내림차순으로 단어는 사전순(오름차순)으로 정렬
wordsDict= sorted(wordsDict.items(), key = lambda x : (-x[1][0], -x[1][1], x[1][2])) # x[0] = 단어, x[1] = 단어 빈도수

for w in wordsDict:
    print(w[0])