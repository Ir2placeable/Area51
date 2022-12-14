# 1783 : 병든 나이트
# https://www.acmicpc.net/problem/1783
import sys
height, width = map(lambda x: int(x), sys.stdin.readline().split(" "))

point = []
def init(a, b):
    if 1 <= a <= height and 1 <= b <= width:
        point.append([a, b])
        init(a+1, b+2)
        init(a+2, b+1)
        init(a-1, b+2)
        init(a-2, b+1)

init(1, 1)
print(point)
print(len(point))
