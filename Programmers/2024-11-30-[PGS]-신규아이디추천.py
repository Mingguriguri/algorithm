def solution(new_id):
    # 1. 대문자 -> 소문자
    answer = new_id.lower()
    print(f"1단계 성공: {answer}")

    # 2단계: 허용되지 않는 문자 제거
    for word in answer:
        if word.islower() or word.isdigit() or word == '-' or word == '_' or word == '.':
            continue
        else:
            answer = answer.replace(word, '')
    print(f"2단계 성공: {answer}")

    # 3단계: 연속된 마침표를 하나로 치환
    temp = ''
    for i in range(len(answer)):
        if i > 0 and answer[i] == '.' and answer[i - 1] == '.':
            continue
        temp += answer[i]
    if temp:
        answer = temp
    print(f"3단계 성공: {answer}")

    # 4단계: 처음과 끝의 마침표 제거
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]

    print(f"4단계 성공: {answer}")

    # 5단계: 빈 문자열 처리
    if not answer:
        answer = 'a' + answer
    print(f"5단계 성공: {answer}")

    # 6단계: 길이 제한
    if len(answer) >= 16:
        answer = answer[:15]  # 15자까지만
    if answer and answer[-1] == '.':
        answer = answer[:-1]  # 맨 마지막 마침표 제거
    print(f"6단계 성공: {answer}")

    # 7단계: 길이 보충
    while len(answer) < 3:
        answer += answer[-1]

    print(f"7단계 성공: {answer}")

    return answer