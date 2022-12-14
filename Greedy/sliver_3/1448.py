# 1448 : 삼각형 만들기
# https://www.acmicpc.net/problem/1448

# a < b + c
n = int(input())
item = []
for i in range(0, n):
    item.append(int(input()))
item.sort(reverse=True)

a, b, c = 0, 1, 2
result = 0
while 1:
    if item[a] < item[b] + item[c]:
        result = item[a] + item[b] + item[c]
        break
    a += 1
    b += 1
    c += 1
    if c == n:
        result = -1
        break

print(result)