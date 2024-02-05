from sys import stdin

n = int(stdin.readline())
trees = []
cnt = 0
for i in range(n):
    trees.append(int(stdin.readline()))
trees.sort()
'''
첫번째 인덱스값과 그 다음 인덱스 값의 차이가 3 이상이라면
트리 놓을 수 있음 트리의 위치는 (두번째-첫번째) 인덱스 값
따라서 트리 놓을 때는 append가 아니라 insert 중간에 인덱스 이용해서 끼워넣기
'''

for i in range(n-1):
    print("i = %d"%i)
    if trees[i+1] - trees[i] >= 3:
        trees.insert(i+1, (trees[i+1] - trees[i] + trees[i-1]))
        cnt += 1
        print(trees, cnt)
print(cnt)