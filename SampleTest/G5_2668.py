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

    flag = False
    nex = arr[i][1]
    while True:
        if nex == start:
            flag = True
            break

        if visited[nex] == 1:
            break

        visited[nex] = 1
        nex = arr[nex][1]

    # using visited
    if not flag:
        continue

    for j in range(n):
        if visited[j] == 1:
            result[j] = 1

print(sum(result))
for i in range(n):
    if result[i] == 1:
        print(i+1)