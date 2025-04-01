import os
import json

SCOREBOARD_FILE = "scoreboard.json"
PR_DATA_FILE = "pr_data.json"

def main():
    # 1. 기존 스코어보드 로드 (파일이 없으면 초기화)
    if os.path.exists(SCOREBOARD_FILE):
        with open(SCOREBOARD_FILE, 'r', encoding='utf-8') as f:
            scoreboard = json.load(f)
    else:
        # 초기에는 DP와 DFS/BFS만 관리하고 싶다면 아래처럼 초기화
        scoreboard = {"DP": [], "DFS/BFS": []}
    print(f"scorebard: {scoreboard}")
    # 2. pr_data.json 파일 로드
    if not os.path.exists(PR_DATA_FILE):
        print(f"{PR_DATA_FILE} 파일이 존재하지 않습니다.")
        exit(1)

    with open(PR_DATA_FILE, 'r', encoding='utf-8') as f:
        pr_data = json.load(f)

    # 3. pr_data의 각 항목을 순회하며 스코어보드 업데이트
    print(f"pr_data: {pr_data}")
    for entry in pr_data:
        print(f"entry: {entry}")
        algorithm = entry["algorithm"]
        problem_id = entry["problem_id"]

        # 스코어보드에 해당 알고리즘 유형이 없으면 동적으로 추가
        if algorithm not in scoreboard:
            scoreboard[algorithm] = []

        # 중복 없이 문제 번호 추가
        if problem_id not in scoreboard[algorithm]:
            scoreboard[algorithm].append(problem_id)
        print(f"scoreboard: {scoreboard}")
        # 4. 업데이트된 스코어보드 저장
        with open(SCOREBOARD_FILE, 'w', encoding='utf-8') as f:
            json.dump(scoreboard, f, ensure_ascii=False, indent=2)

        print("scoreboard.json 업데이트 완료!")

if __name__ == '__main__':
    main()
