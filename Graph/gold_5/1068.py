# 1068 : 트리
# https://www.acmicpc.net/problem/1068

# 5
# -1 0 0 1 1
# 2

import sys

n = int(sys.stdin.readline())
trees = list(map(lambda x: int(x), sys.stdin.readline().split()))
target = int(sys.stdin.readline())
# -2 : 부러진 노드를 의미한다.
trees[target] = -2
print(trees)