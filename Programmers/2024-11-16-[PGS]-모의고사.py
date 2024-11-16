def solution(answers):
    supoja1 = [1, 2, 3, 4, 5]  # 수포자 1이 찍는 방식
    supoja2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 수포자 2가 찍는 방식
    supoja3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 수포자 3이 찍는 방식

    scores = [0, 0, 0]  # 수포자 1, 2, 3의 점수

    answer = []  # 가장 높은 점수를 받은 사람 배열

    # 점수 계산
    for i in range(len(answers)):
        # 수포자 1 점수 계산
        if supoja1[i % len(supoja1)] == answers[i]:
            scores[0] += 1

        # 수포자 2 점수 계산
        if supoja2[i % len(supoja2)] == answers[i]:
            scores[1] += 1

        # 수포자 3 점수 계산
        if supoja3[i % len(supoja3)] == answers[i]:
            scores[2] += 1

    # 가장 높은 점수
    max_score = max(scores)

    for i in range(len(scores)):  # 높은 점수를 받은 사람은 answer 배열에 추가
        if scores[i] == max_score:
            answer.append(i + 1)

    return answer