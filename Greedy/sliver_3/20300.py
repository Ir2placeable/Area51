# 20300 : 서강근육맨
# https://www.acmicpc.net/problem/20300
import sys

n = int(sys.stdin.readline())
item_list = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
item_list.sort()

val = 0
if len(item_list) % 2 == 1:
    for i in range(0, (n-1)//2):
        val = max(val, item_list[i] + item_list[n-i-2])
    val = max(val, item_list[-1])
else:
    for i in range(0, n//2):
        val = max(val, item_list[i] + item_list[n-i-1])

print(val)