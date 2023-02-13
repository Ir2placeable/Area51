# 트리, 구현

# 13분 컷

from collections import deque

t = int(input())
for test_case in range(1, t+1):
    v, e, v1, v2 = map(lambda x: int(x), input().split())
    edges = list(map(lambda x: int(x), input().split()))
    trees = [[] for _ in range(v+1)]

    for i in range(0, len(edges), 2):
        trees[edges[i]].append(edges[i+1])

    parents = []
    cur = v1
    isParent = True
    while isParent:
        isParent = False
        for i in range(v+1):
            if cur in trees[i]:
                parents.append(i)
                cur = i
                isParent = True
                break

    target_vertex = 0
    cur = v2
    while True:
        if cur in parents:
            target_vertex = cur
            break

        for i in range(v+1):
            if cur in trees[i]:
                cur = i
                break

    count = 0
    queue = deque([target_vertex])

    while queue:
        qv = queue.popleft()
        count += 1

        for nv in trees[qv]:
            queue.append(nv)

    result = [target_vertex, count]
    print("#%d %d %d" % (test_case, result[0], result[1]))