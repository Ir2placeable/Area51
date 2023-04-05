import sys

H, W, N, M = map(lambda x: int(x), sys.stdin.readline().split())

a, b = 0, 0
for i in range(0, H, N+1):
    a += 1
for j in range(0, W, M+1):
    b += 1

print(a * b)