# 2885 : 초콜릿 식사
# https://www.acmicpc.net/problem/2885
import sys

k = int(sys.stdin.readline())

items = [1]
i = 1
while i < k:
    i *= 2
    items.append(i)

max_choco = items[-1]
count = 0
while k > 0:
    temp = items.pop()

    if k == temp:
        break

    if k > temp:
        k -= temp
    count += 1
print(max_choco, count)


# 1 1 0 : 1
# 2 2 0 : 2
# 3 4 2 : 2 + 1
# 4 4 0 : 4
# 5 8 3 : 4 + 1
# 6 8 2 : 4 + 2
# 7 8 3 : 4 + 2 + 1
# 8 8 0 : 8
# 9 16 4 : 8 + 1
# 10 16 4 : 8 + 2