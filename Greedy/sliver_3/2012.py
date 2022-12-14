# 2012 : 등수 매기기
# https://www.acmicpc.net/problem/2012

n = int(input())
rank = []
for i in range(0, n):
    rank.append(int(input()))
rank.sort()

val = 0
for i in range(0, n):
    val += max(i+1 - rank[i], rank[i] - i - 1)

print(val)