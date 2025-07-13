count = 0


def solution(numbers, target):
    global count
    backtracking(0, 0, numbers, target)

    return count


def backtracking(idx, curr_sum, numbers, target):
    global count

    # 종료 조건
    if idx == len(numbers):
        if curr_sum == target:
            count += 1
        return

    backtracking(idx + 1, curr_sum + numbers[idx], numbers, target)  # 선택지 1: 현재 숫자 더하기
    backtracking(idx + 1, curr_sum - numbers[idx], numbers, target)  # 선택지 2: 현재 숫자 빼기

