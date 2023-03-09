from collections import deque

test_case = int(input())
for case_number in range(1, test_case + 1):
    n = int(input())
    temp = list(map(lambda x: int(x), input().split()))

    tree = [[] for _ in range(n+1)]
    for i in range(len(temp)):
        tree[temp[i]].append(i + 2)

    nodes = [{'parent': 0, 'depth': 0, 'self': i} for i in range(n+1)]
    queue = deque([[0, 1]])

    # nodes 구하기
    while queue:
        cur_depth, cur_node = queue.popleft()

        for child_node in tree[cur_node]:
            nodes[child_node]['parent'] = cur_node
            nodes[child_node]['depth'] = cur_depth + 1
            queue.append([cur_depth + 1, child_node])

    PATH = [1]
    queue = deque([1])
    while queue:
        cur_node = queue.popleft()
        for next_node in tree[cur_node]:
            queue.append(next_node)
            PATH.append(next_node)

    result = 0
    cur_point = PATH.pop()
    while PATH:
        temp_traverse_count = 0
        next_point = PATH.pop()

        node1, node2 = nodes[cur_point], nodes[next_point]
        while node1['depth'] > node2['depth']:
            temp_traverse_count += 1
            node1 = nodes[node1['parent']]
        while node2['depth'] < node2['depth']:
            temp_traverse_count += 1
            node2 = nodes[node2['parent']]

        while node1['parent'] != node2['parent']:
            temp_traverse_count += 2
            node1 = nodes[node1['parent']]
            node2 = nodes[node2['parent']]

        if node1['self'] != node2['self']:
            temp_traverse_count += 2

        result += temp_traverse_count
        cur_point = next_point

    print("#%d %s" %(case_number, str(result)))