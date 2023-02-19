# https://www.acmicpc.net/problem/20125
import sys

n = int(sys.stdin.readline())
maps = []
for _ in range(n):
    maps.append(list(sys.stdin.readline().rstrip()))

heart_y, heart_x = 0, 0
for y in range(n):
    f = False
    for x in range(n):
        if maps[y][x] == '*':
            heart_y = y + 1
            heart_x = x + 0
            f = True
            break
    if f:
        break

print(heart_y+1, heart_x+1)
result = []
temp = 0
for i in range(heart_x):
    if maps[heart_y][i] == '*':
        temp += 1
result.append(temp)
temp = 0
for i in range(heart_x+1, n):
    if maps[heart_y][i] == '*':
        temp += 1
result.append(temp)
temp = 0
for i in range(heart_y+1, n):
    if maps[i][heart_x] == '*':
        temp += 1
result.append(temp)
temp = 0
for i in range(heart_y+1, n):
    if maps[i][heart_x-1] == '*':
        temp += 1
result.append(temp)
temp = 0
for i in range(heart_y+1, n):
    if maps[i][heart_x+1] == '*':
        temp += 1
result.append(temp)
print(*result)