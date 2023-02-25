# https://www.acmicpc.net/problem/10971

# Prim 알고리즘을 생각했지만, Prim 은 무향 그래프에 적용하는 것이다.
# 도시를 거칠 순서를 정해두고, 비용을 계산하는 문제이다. -> 순열임 -> 백트래킹

import sys


def backTracking(start, prev, cur_cost, visited):
    global result

    # 이미 도시순회 비용이 크다
    if cur_cost > result:
        return

    # 모든 도시를 방문헀다
    if len(visited) == n:
        if getCost[prev][start] != 0:
            cur_cost += getCost[prev][start]
            result = min(result, cur_cost)
        return

    # 도시를 순회한다.
    for i in range(n):
        if i in visited:
            continue
        if getCost[prev][i] == 0:
            continue

        visited.append(i)
        backTracking(start, i, cur_cost + getCost[prev][i], visited)
        visited.remove(i)


n = int(sys.stdin.readline())
getCost = [list(map(lambda x: int(x), sys.stdin.readline().split())) for _ in range(n)]
cities = [i for i in range(n)]

result = sys.maxsize
for start_city in cities:
    backTracking(start_city, start_city, 0, [start_city])

print(result)