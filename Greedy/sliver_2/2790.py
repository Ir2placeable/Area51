# 2790 : F7
# https://www.acmicpc.net/problem/2790
import sys

n = int(sys.stdin.readline())
scores = []
for i in range(n):
    scores.append(int(sys.stdin.readline()))
scores.sort()

max_score = 0
for i in range(0, n):
    max_score = max(max_score, scores[i] + n-i)

can_win = 0
for score in scores:
    if score + n >= max_score:
        can_win += 1

print(can_win)