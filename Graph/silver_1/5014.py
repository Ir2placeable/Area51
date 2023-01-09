# 5014 : 스타트링크
# https://www.acmicpc.net/problem/5014

total, start, target, up, down = map(lambda x: int(x), input().split(" "))
# F, S, G, U, D = map(lambda x: int(x), input().split(" "))
# F : 총 층
# S : 시작 층
# G : 목표 층
# U : 위로 몇 칸
# D : 아래로 몇 칸
# 10 1 10 2 1

from collections import deque
visited = [0 for _ in range(total + 1)]

queue = deque([start])
while queue:
    point = queue.popleft()

    moving_case = [point + up, point - down]
    for case in moving_case:
        if case < 0 or case > total:
            continue

        if visited[case] == 0:
            queue.append(case)
            visited[case] = visited[point] + 1

if visited[target] == 0:
    print('use the stairs')
else:
    print(visited[target])