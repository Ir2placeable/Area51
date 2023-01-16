# 16395 : 파스칼의 삼각형
# https://www.acmicpc.net/problem/16395

n, k = map(lambda x: int(x), input().split(" "))

result = [[1 for _ in range(i)] for i in range(1, n+1)]
for i in range(2, n):
    for j in range(1, i):
        result[i][j] = result[i-1][j-1] + result[i-1][j]

print(result[n-1][k-1])