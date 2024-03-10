def solution(k, tangerine):
    answer = 0
    
    '''
    딕셔너리에 key크기, value 개수를 저장한다.
    딕셔너리를 value를 크기가 큰 순으로 정렬한다.
    '''
    box = {}
    for t in tangerine:
        if t in box:
            box[t] += 1
        else:
            box[t] = 1
    
    box = dict(sorted(box.items(), key=lambda x: x[1], reverse=True))

    '''
    k에 개수 값을 빼가고, 뺄 때마다 answer+=1한다.
    k가 0보다 작아지면 바로 answer return한다
    '''
    for size in box:
        if k <= 0:
            return answer
        k -= box[size]
        answer += 1
    return answer