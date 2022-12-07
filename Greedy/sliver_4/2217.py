# 2217 : 로프
# https://www.acmicpc.net/problem/2217

N = int(input())

ropes = []
for i in range(0, N):
    ropes.append(int(input()))

ropes.sort(reverse=True)
max_weight = 0
for i in range(0, N):
    temp = ropes[i] * (i+1)
    max_weight = max(max_weight, temp)

print(max_weight)