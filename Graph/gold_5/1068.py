# 1068 : 트리
# https://www.acmicpc.net/problem/1068
import sys
from collections import deque

n = int(sys.stdin.readline())
parents = list(map(lambda x: int(x), sys.stdin.readline().split()))
x = int(sys.stdin.readline())
# print(parents)

# x : 부러진 노드를 의미함
# parents에서 x를 가지고 있는 노드 또한 부러진 노드로 변경

queue = deque([x])
while queue:
    broken_node = queue.popleft()
    parents[broken_node] = -2

    while broken_node in parents:
        target_index = parents.index(broken_node)
        queue.append(target_index)
        parents[target_index] = -2

leaf_node = 0
for node in range(0, n):
    if parents[node] != -2 and node not in parents:
        leaf_node += 1
print(leaf_node)