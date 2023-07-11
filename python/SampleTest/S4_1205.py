# https://www.acmicpc.net/problem/1205
import sys

n, taesu, cut = map(lambda x: int(x), sys.stdin.readline().split())
scores = []
if n > 0:
    scores = list(map(lambda x: int(x), sys.stdin.readline().split()))
scores.append(taesu)
scores.sort(reverse=True)

target = 0
for i in range(n+1):
    if scores[i] == taesu:
        target = i

ranking = [1 for _ in range(n + 1)]
for i in range(len(ranking)):
    for j in range(i):
        if scores[i] < scores[j]:
            ranking[i] += 1
ranking = ranking[:min(len(ranking), cut)]

result = -1
if target < len(ranking):
    result = ranking[target]
print(result)