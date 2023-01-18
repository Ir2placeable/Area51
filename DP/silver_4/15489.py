# 15489 : 파스칼 삼각형
# https://www.acmicpc.net/problem/15489

r, c, w = map(lambda x: int(x), input().split())
height0 = r-1
width0 = c-1
height1 = r-1 + w
# print(height0, width0, height1)

pascal = [[1] * i for i in range(1, height1+1)]
for i in range(1, height1):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
# print(pascal)

result = 0
index = 1
for i in range(height0, height1):
    for j in range(width0, width0+index):
        # print(pascal[i][j])
        result += pascal[i][j]
    index += 1

print(result)