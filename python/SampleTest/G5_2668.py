# https://www.acmicpc.net/problem/2668
# 53분

import sys

n = int(sys.stdin.readline())
arr = [[i, int(sys.stdin.readline()) - 1] for i in range(n)]

result = [0 for _ in range(n)]
for i in range(n):
    start = arr[i][0]
    visited = [0 for _ in range(n)]
    visited[i] = 1

    # circular 조건 체크
    isCircular = False
    picked_number = arr[i][1]
    while True:
        # 뽑은 숫자들이 circular 한 경우 -> 문제 조건에 부합한다.
        if picked_number == start:
            isCircular = True
            break

        # 뽑은 숫자가 이미 뽑혀 있는 경우 -> 문제 조건에 부합하지 않는다.
        if visited[picked_number] == 1:
            break

        # 뽑은 숫자를 기록하고, 다음 숫자를 뽑는다.
        visited[picked_number] = 1
        nex = arr[picked_number][1]

    if not isCircular:
        continue

    # 뽑은 숫자들이 circular 한 경우 -> 뽑은 숫자들을 기록한다.
    for j in range(n):
        if visited[j] == 1:
            result[j] = 1

print(sum(result))
for i in range(n):
    if result[i] == 1:
        print(i+1)