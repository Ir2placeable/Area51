from collections import deque

test_case = int(input())
for case_number in range(1, test_case + 1):
    n = int(input())
    temp = list(map(lambda x: int(x), input().split()))

    parents = [0, 0] + temp
    print('parents : ', parents)

    tree = [[] for _ in range(n+1)]
    for i in range(len(temp)):
        tree[temp[i]].append(i + 2)
    print('tree : ', tree)

    nodes = [[] for _ in range(n+1)]
    nodes[1] = [0, 0]
    queue = deque([[0, 1]])

    while queue:
        depth, node = queue.popleft()

        for next_node in tree[node]:
            nodes[next_node] = [depth + 1, node]
            queue.append([depth + 1, next_node])
    print('nodes : ', nodes)

    ancestors = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            ancestors[j][i] = ancestors[ancestors[j][i - 1]][i - 1]

    print('ancestors : ', ancestors)