# 11497 : 통나무 건너뛰기
# https://www.acmicpc.net/problem/11497

# 통나무를 세울 때, 가장 큰 값을 가운데로 두고, 왼쪽 오른쪽 번갈아 가면서 넣으면 되지 않을까? 라는 막연한 아이디어 부터 시작해보자
import sys

test_case = int(sys.stdin.readline())
for i in range(test_case):
    n = int(sys.stdin.readline())
    items = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
    items.sort()

    direction = 0
    logs = []
    while len(items) > 0:
        if direction == 0:
            logs.append(items.pop())
        else:
            logs.insert(0, items.pop())
        direction = (direction+1) % 2

    logs.append(logs[0])

    max_diff = 0
    for j in range(0, n):
        max_diff = max(max_diff, max(logs[j] - logs[j+1], logs[j+1] - logs[j]))

    print(max_diff)