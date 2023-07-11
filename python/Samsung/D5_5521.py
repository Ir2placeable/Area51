from collections import deque

test_case = int(input())
for case_number in range(1, 1 + test_case):
    n, m = map(lambda x: int(x), input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(lambda x: int(x), input().split())
        graph[a].append(b)
        graph[b].append(a)

    invited = [False for _ in range(n+1)]
    invited[1] = True
    queue = deque([[0, 1]])
    result = 0

    while queue:
        connected_count, _from = queue.popleft()
        if connected_count == 2:
            continue

        for _to in graph[_from]:
            if invited[_to]:
                continue

            invited[_to] = True
            result += 1
            queue.append([connected_count + 1, _to])

    print("#%d %d" % (case_number, result))