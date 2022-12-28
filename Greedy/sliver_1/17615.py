# 17615 : 볼 모으기
# https://www.acmicpc.net/problem/17615

import sys

n = int(sys.stdin.readline())
balls = sys.stdin.readline().rstrip()
moves = 10000000000

temp = balls.rstrip('R')
moves = min(moves, temp.count('R'))
temp = balls.rstrip('B')
moves = min(moves, temp.count('B'))
temp = balls.lstrip('R')
moves = min(moves, temp.count('R'))
temp = balls.lstrip('B')
moves = min(moves, temp.count('B'))

print(moves)