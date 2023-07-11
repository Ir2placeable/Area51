# https://www.acmicpc.net/problem/8979
import sys

n, k = map(lambda x: int(x), sys.stdin.readline().split())

nations = []
for _ in range(n):
    nations.append(list(map(lambda x: int(x), sys.stdin.readline().split())))
nations.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

ranking = [0 for _ in range(n+1)]
prev = []
rank = 0
add = 1
for nation in nations:
    if prev != nation[1:]:
        rank += add
        add = 1
    else:
        add += 1

    ranking[nation[0]] = rank
    prev = nation[1:]

print(ranking[k])