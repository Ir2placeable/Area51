# 1068 : 트리
# https://www.acmicpc.net/problem/1068
import sys
from collections import deque

# 본 문제의 문제 풀이 방식은 다음과 같다.
# 1. 부러진 노드와 해당 모든 자식들을 부러뜨린다. -> -2로 표시한다.
# 2-1. 모든 노드를 탐색한다. 부러진 노드 이거나, 해당 노드의 자식이 없는 경우에 -> 리프 노드로 취급한다.
# 2-2. 해당 노드의 자식이 없다 == parents 리스트의 해당 노드가 없다.


n = int(sys.stdin.readline())
parent_node_list = list(map(lambda x: int(x), sys.stdin.readline().split()))
x = int(sys.stdin.readline())

# 1. BFS 방식으로 노드를 부러뜨린다.
parent_node_list[x] = -2

queue = deque([x])
while queue:
    broken_node = queue.popleft()

    while broken_node in parent_node_list:
        target_index = parent_node_list.index(broken_node)
        queue.append(target_index)
        parent_node_list[target_index] = -2

# 2. 리프 노드를 센다.
leaf_node = 0
for current_node in range(0, n):
    if (parent_node_list[current_node] != -2) and (current_node not in parent_node_list):
        leaf_node += 1
print(leaf_node)