# https://www.acmicpc.net/problem/2110

import sys

n, c = map(lambda x: int(x), sys.stdin.readline().split())
locations = []
for _ in range(n):
    locations.append(int(sys.stdin.readline()))
locations.sort()
print(locations)

diff = []
for i in range(n-1):
    diff.append(locations[i+1] - locations[i])
print(diff)