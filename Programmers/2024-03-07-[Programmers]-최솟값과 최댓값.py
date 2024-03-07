def solution(s):
    '''
    1. 문자열 형태로 들어오는 숫자들을 `map` 함수와 `split` 함수를 이용해 분리해주고, 이 값들을 리스트로 저장한다.
    2. 리스트 내에서 최솟값과 최댓값을 answer리스트에 저장한다.
    3. answer리스트에 저장된 값이 또다시 문자열 형태로 출력되어야 한다.
        이때 필요한 것은 `join`과 `map`이다. int형을 join으로 묶을 수 없기 때문에, str형태로 형변환하면서 map을 찢어놔준 후, join으로 공백을 두고 묶어주면 된다.
    '''    
    nums = list(map(int, s.split()))
    #print(nums)
    answer = [min(nums), max(nums)]
    #print(answer)
    #print(' '.join(map(str, answer)))
    return ' '.join(map(str, answer))