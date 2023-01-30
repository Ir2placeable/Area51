# 무거운 박스는 무게 제한이 큰 크레인이 옮겨야 한다. -> 정렬이 필요하다.
# 모든 박스를 옮기는 데 최소값을 구해야 한다 -> 그리디 문제.
# 정렬 + 그리디 / 또는 우선순위 큐를 사용할 수 있을 것 같다.

import sys

n = int(sys.stdin.readline())
cranes = list(map(lambda x: int(x), sys.stdin.readline().split()))
m = int(sys.stdin.readline())
boxes = list(map(lambda x: int(x), sys.stdin.readline().split()))

cranes.sort()
boxes.sort()

max_weight = max(cranes)

time = list(map(lambda x: [0, x], cranes))
while boxes:
    if boxes[-1] > max_weight:
        time = [[-1, -1]]
        break

    box = boxes.pop()
    for i in range(0, n):
        if time[i][1] >= box:
            time[i][0] += 1
            break

    time.sort(key=lambda x: x[0])

print(max(time)[0])