# https://www.acmicpc.net/problem/10157

# c, r = 7, 6
# k = x, y

# 1 : 1, 1
# 2 : 1, 2
# 3 : 1, 3
# 4 : 1, 4
# 5 : 1, 5
# 6 : 1, 6

# 7 : 2, 6
# 8 : 3, 6
# 9 : 4, 6
# 10 : 5, 6
# 11 : 6, 6
# 12 : 7, 6

# 13 : 7, 5
# 14 : 7, 4

import sys
x, y = map(lambda x: int(x), sys.stdin.readline().split())
k = int(sys.stdin.readline())

min_x, max_x = 1, x
min_y, max_y = 1, y
# 1,y / x,y / x,1 / 2,1 / 2,y-1 / x-1,y-1 /

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cur_x, cur_y, cur_d = 1, 1, 0

index = 1
over = False
while index < k:
    if cur_d == 0 and cur_y == max_y:
        cur_d = (cur_d + 1) % 4
        min_x += 1
    elif cur_d == 1 and cur_x == max_x:
        cur_d = (cur_d + 1) % 4
        max_y -= 1
    elif cur_d == 2 and cur_y == min_y:
        cur_d = (cur_d + 1) % 4
        max_x -= 1
    elif cur_d == 3 and cur_x == min_x:
        cur_d = (cur_d + 1) % 4
        min_y += 1

    cur_x = cur_x + dx[cur_d]
    cur_y = cur_y + dy[cur_d]

    index += 1

    if index > x * y:
        over = True
        break

if over:
    print(0)
else:
    print(cur_x, cur_y)