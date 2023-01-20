# https://www.acmicpc.net/problem/1238

# BFS 알고리즘을 통해 시작지점 - 목표지점 까지의 최단거리를 구해야한다.
# 목표지점은 입력값으로 고정되어 있다.
# 시작지점은 1~N 사이로 변경된다.

# BFS + 브루트포스 알고리즘을 섞은 유형의 문제이다.
# 다익스트라 알고리즘 + 브루트포스 알고리즘인 것 같다.

# 일단 0에서 target으로 가는 다익스트라 알고리즘을 작성해야한다.
# 그 다음, 0을 -> N까지 순회하는 방식으로 변경한다.

import sys
import heapq

height, width, target = map(lambda x: int(x), sys.stdin.readline().split())
maps = [[] for j in range(height+1)]
for _ in range(width):
    _from, _to, _cost = map(lambda x: int(x), sys.stdin.readline().split())
    maps[_from].append([_cost, _to])
# print(maps)


def party(_from, _to):
    return dijkstra(_from, _to) + dijkstra(_to, _from)

def dijkstra(start, end):
    total_weight = [sys.maxsize for _ in range(height+1)]
    total_weight[0] = 0
    total_weight[start] = 0

    queue = [[0, start]]
    while queue:
        cur_weight, cur_vertex = heapq.heappop(queue)

        for add_weight, next_vertex in maps[cur_vertex]:
            if total_weight[next_vertex] < cur_weight + add_weight:
                continue
            total_weight[next_vertex] = cur_weight + add_weight
            heapq.heappush(queue, [cur_weight + add_weight, next_vertex])

    return total_weight[end]

result = 0
for person in range(1, height+1):
    result = max(result, party(person, target))
print(result)