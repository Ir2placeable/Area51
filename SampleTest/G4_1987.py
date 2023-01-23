# https://www.acmicpc.net/problem/1987

# BFS 알고리즘을 베이스로 한 문제이다.
# 통과조건에 이때까지 지나가지 않은 알파벳을 기준으로 한다. -> 알파벳은 26개로 고정되어 있으므로 미리 선언해서 사용한다.
# 26개를 일일히 적기는 귀찮으므로 ASCII를 사용한 배열을 만든다.


import sys
from collections import deque

height, width = map(lambda x: int(x), sys.stdin.readline().split())
maps = []
for _ in range(height):
    temp = list(sys.stdin.readline().strip())
    temp2 = []
    for temp3 in temp:
        temp2.append(temp3)
    maps.append(temp2)
print(maps)

visited = [0 for i in range(26)]
visited[ord(maps[0][0])] = 1
queue = deque([0, 0, visited])
print(visited)