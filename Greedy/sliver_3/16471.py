# 16471 : 작은 수 내기
# https://www.acmicpc.net/problem/16471
import sys

n = int(sys.stdin.readline())
home = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
away = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))

home.sort()
away.sort()

winning_score = (n+1)//2
home = home[:winning_score]
away = away[-1 * winning_score:]

flag = True
for i in range(0, winning_score):
    if home[i] >= away[i]:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')