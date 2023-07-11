# https://www.acmicpc.net/problem/1966

# 우선도가 높은 것을 먼저 사용한다. -> 우선순위 큐를 이용하여 구한다.
# 중요도가 같은 문서가 있기 때문에, 단순 sort / heapq 로는 중복된 번호의 순서를 정할 수 없다.
# 따라서 문제가 설명하는 흐름을 그대로 구현해야 한다. -> deque 사용한다.
# 문서의 최대 개수는 100이기 때문에 전부 탐색해도 무관하다. -> 완전 탐색이 가능하다.

import sys
from collections import deque

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    n, target = map(lambda x: int(x), sys.stdin.readline().split())
    temp = list(map(lambda x: int(x), sys.stdin.readline().split()))

    # docs : priority / index
    docs = deque([])
    for i in range(n):
        docs.append([temp[i], i])

    count = 0
    while docs:
        doc = docs.popleft()

        # docs 에 높은 우선순위가 있는 경우,
        if list(filter(lambda x: x[0] > doc[0], docs)):
            docs.append(doc)
            continue

        count += 1
        if doc[1] == target:
            break

    print(count)