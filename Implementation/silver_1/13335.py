# https://www.acmicpc.net/problem/13335
import sys
from collections import deque

n, w, l = map(lambda x: int(x), sys.stdin.readline().split())
trucks = deque(map(lambda x: int(x), sys.stdin.readline().split()))
bridge = deque([0 for i in range(w)])

required_time = 0
while trucks:
    bridge.popleft()
    if sum(bridge) + trucks[0] <= l:
        bridge.append(trucks.popleft())
    else:
        bridge.append(0)

    required_time += 1
print(required_time + w)