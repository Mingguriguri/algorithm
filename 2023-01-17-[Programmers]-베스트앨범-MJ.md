# 베스트앨범

progress: In progress
review: 🥜
site: 프로그래머스
upload: Yes
등급: Level3
링크: https://school.programmers.co.kr/learn/courses/30/lessons/42579
유형: 해시 테이블
작성일시: 2023년 1월 20일 오후 1:26

# [고득점 kit - 해시 - 베스트앨범](https://school.programmers.co.kr/learn/courses/30/lessons/42579)

# 📖Problems

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

### 제한사항

- genres[i]는 고유번호가 i인 노래의 장르입니다.
- plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
- genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
- 장르 종류는 100개 미만입니다.
- 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
- 모든 장르는 재생된 횟수가 다릅니다.

### 입출력 예

| genres | plays | return |
| --- | --- | --- |
| ["classic", "pop", "classic", "classic", "pop"] | [500, 600, 150, 800, 2500] | [4, 1, 3, 0] |

### 입출력 예 설명

classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.

- 고유 번호 3: 800회 재생
- 고유 번호 0: 500회 재생
- 고유 번호 2: 150회 재생

pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.

- 고유 번호 4: 2,500회 재생
- 고유 번호 1: 600회 재생

따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

- 장르 별로 가장 많이 재생된 노래를 최대 두 개까지 모아 베스트 앨범을 출시하므로 2번 노래는 수록되지 않습니다.

# 🔍Approach

1. return해야 할 answer : 많이 재생된 장르에서 재생이 많이 된 노래의 고유번호
2. **flow** 
- generes와 play를 한 리스트에 저장한다. [classic, 500], [pop, 600], [classic, 150], [classic,800], [pop,2500]
- 입력받은 genres를 set함수를 통해 중복값을 제거한다.

play로 받은 리스트 값을 인덱스와 함께 저장한다.(enumerate -> [고유번호, 재생횟수])

- genere_play = {} 딕셔너리를 생성한다. genere_play = {classic = [[3, 800], [0, 500], …], pop = [[4, 2500],[1,600]]}
    - key : genere
    - value : [고유번호, 재생횟수]를 담고 있는 리스트
- playlist 리스트에 고유번호와 재생횟수를 담는다. 해당 리스를 sorted()를 이용해서 정렬한다.
- **장르끼리 총 재생횟수 비교**
- **장르 내에 있는 노래끼리 비교**
- 많이 재생된 장르부터 많이 재생된 노래의 고유번호를 return, 최대 2곡까지만 return

1. **장르끼리 총 재생횟수 비교 genere_count = {}key: 장르 , value: 총 재생횟수 -> sorted(1번dict.items(), reverse=True) -> 장르끼리 비교 완료!**
2. **장르 내 노래 비교 songs_count = {} key : generes , value : 1번 딕셔너리 -> sort -> 2개 픽해서 -> answer에 append**

## 🚩My submission

```python
def solution(genres, plays):
    answer = []
    genere_count = {}
    songs_count = {}
    
    for _ in zip(genres,plays):
        genere_count.append({genres : plays})
    playlist = sorted(genere_count.items(), reverse = True)
        
    for _ in zip(genres, plays):
        songs_count.append({i : playlist[i]})
        
    songs = sorted(songs_count.items(), reverse = True)
    
    for i in range(songs_count):
        answer.append(songs_cont[i])
        
    return answer
```

**>>** AttributeError: 'dict' object has no attribute 'append'

## 🚩Others submission

```python
def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
```

# 💡TIL

- 딕셔너리에 items() 메서드를 사용해주면 {"key" : value}의 형태를 [(key, value)]의 형태로 만들어 준다.
- 이를 sorted해주면 key값을 기준으로 오름차순으로 정렬한다. value값으로 정렬하려면 `lambda`를 사용해주면 된다.
    
    ```python
    sorted(d.items(), key=lambda x : x[1])
    ```
    
    - `lamda`
    
    ```python
    # lambda 매개변수 : 표현식
    
    >>> (lambda x,y: x + y)(10, 20)
    30
    ```