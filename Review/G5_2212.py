# 집중국의 수신 가능 영역 최소화 -> 그리디 문제

# 집중국의 수신 거리를 최소하기 위하기 위해서는 -> 두 좌표간 차이가 큰 곳에 설치해야 한다.
# 1. 좌표를 오름차순으로 정렬한다
# 2. 두 좌표간 거리 차이를 구한다.
# 3. 거리 차이가 큰 두 좌표에 각각 집중국을 설치한다. 집중국의 개수를 차감한다. 집중국의 개수가 0이 되면 멈춘다.

import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
locations = list(map(lambda x: int(x), sys.stdin.readline().split()))
locations.sort()

diffs = []
for i in range(0, n-1):
    diffs.append(locations[i+1] - locations[i])
diffs.sort()

while diffs and k > 1:
    diffs.pop()
    k -= 1
print(sum(diffs))