# 20044 : Project Teams
# https://www.acmicpc.net/problem/20044

n = int(input())

items = list(map(lambda x: int(x), input().split(" ")))
items.sort()

min_val = 1000000000
for i in range(0, n):
    min_val = min(min_val, (items[i] + items[2*n-i-1]))
print(min_val)