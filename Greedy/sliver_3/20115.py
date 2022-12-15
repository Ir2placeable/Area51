# 20115 : 에너지 드링크
# https://www.acmicpc.net/problem/20115
import sys

n = int(sys.stdin.readline())
drink_list = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
drink_list.sort(reverse=True)

total_drink = drink_list[0]
for i in range(1, n):
    total_drink += drink_list[i] / 2

print(total_drink)