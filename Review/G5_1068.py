# 노드는 최대 50개 이다 -> 노드로 리스트를 만든다. -> node = []
# 각 노드에는 부모의 노드를 저장해둔다. -> node[i] = 부모노드번호
# 특정 노드가 루트 노드인 경우, node[i] = -1 이다.
# node[삭제할 노드번호] = -2 로 설정한다.
# node 리스트는 결국, 자기 부모를 가르키는 리스트가 된다.

# DFS 방식으로 특정 노드가 루트 노드로 이어져있는지 확인한다. -> 중복 카운팅 되는 경우가 있다.
# 루트 노드에서부터 ~ 자식이 없는 노드까지 체크한다.
# 특정 노드의 index가 node 리스트에 없으면 -> 해당 노드는 부모 노드가 아니라는 의미이다. -> 즉, 리프 노드이다.

import sys

n = int(sys.stdin.readline())
node = list(map(lambda x: int(x), sys.stdin.readline().split()))
x = int(sys.stdin.readline())
node[x] = -2


def dfs(index):
    global leaf_nodes
    if index not in node:
        leaf_nodes += 1
        return

    for i in range(n):
        if node[i] == index:
            dfs(i)


leaf_nodes = 0
for node_index in range(n):
    # 루트 노드인 경우 -> 리프 노드를 체크한다.
    if node[node_index] == -1:
        dfs(node_index)
print(leaf_nodes)