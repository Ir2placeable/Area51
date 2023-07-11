# https://www.acmicpc.net/problem/1976

# 도착 여부 판단하기 -> DFS 알고리즘 사용하는 것으로 보임
# 목적지가 1개가 아닌 여러개임 -> 여러개를 쪼개서 n번 수행하자

# 메모리 초과 발생, 다시 생각해보니 특정 시작점에서 갈 수 있는 최종목적지를 만들어 둘 수 있을 것 같음.
# 여기서 좀 더 생각해보면, 한 목적지에서 갈 수 있는 다른 목적지는 모두 한 묶음으로 따질 수 있음.
# 결과적으로, journey에 있는 수들이 한 묶음인지 판단하면 되는 것임.
# 이떄, 특정 시작점은 항상 journey[0] 으로 고정되어 있음.

import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
maps = [[] for _ in range(n)]
for i in range(n):
    temp = list(map(lambda x: int(x), sys.stdin.readline().split()))
    for j in range(n):
        if temp[j] == 1:
            maps[i].append(j)
journey = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))


def dfs(x):
    for next in maps[x]:
        if not visited[next]:
            visited[next] = True
            dfs(next)


start = journey[0]
visited = [False for _ in range(n)]
visited[start] = True
dfs(start)

result = 'YES'
for destination in journey:
    if not visited[destination]:
        result = 'NO'
        break
print(result)