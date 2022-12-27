# 1052 : 물병
# https://www.acmicpc.net/problem/1052

import sys

n, k = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))

list2 = []
i2 = 1
while i2 <= n:
    list2.append(i2)
    i2 *= 2

list3 = []
while n > 0:
    temp = list2.pop()
    if n >= temp:
        list3.append(temp)
        n -= temp

bottles = 0
while len(list3) > k:
    a = list3.pop()
    b = list3.pop()
    bottles += b - a
    list3.append(2*b)

print(bottles)