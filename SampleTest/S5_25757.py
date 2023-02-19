# https://www.acmicpc.net/problem/25757
import sys

n, game = sys.stdin.readline().split()
players = set()
for _ in range(int(n)):
    players.add(sys.stdin.readline().rstrip())
k = len(players)

result = 0
if game == 'Y':
    result = k
elif game == 'F':
    if k >= 2:
        result = k // 2
elif game == 'O':
    if k >= 3:
        result = k // 3
print(result)