# 1012 : 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys

test_case = int(sys.stdin.readline())
for test_index in range(test_case):
    m, n, k = map(lambda t: int(t), sys.stdin.readline().rstrip().split(" "))

    graph = []
    for y in range(n):
        temp = []
        for x in range(m):
            temp.append(0)
        graph.append(temp)

    for _ in range(k):
        a, b = map(lambda t: int(t), sys.stdin.readline().rstrip().split(" "))
        graph[b][a] = 1
    # print(graph)

    bugs = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                # print('now point : ', x, y)
                bugs += 1
                graph[y][x] = 0

                queue = [[y, x]]
                while queue:
                    qy, qx = queue.pop(0)
                    # print('q',qy, qx)
                    k -= 1

                    for _x in range(max(0, qx - 1), min(m, qx + 2)):
                        if graph[qy][_x] == 1:
                            # print('check point : ', _x, qy)
                            graph[qy][_x] = 0
                            queue.append([qy, _x])
                    for _y in range(max(0, qy - 1), min(n, qy + 2)):
                        if graph[_y][qx] == 1:
                            # print('check point : ', qx, _y)
                            graph[_y][qx] = 0
                            queue.append([_y, qx])
    print(bugs)
