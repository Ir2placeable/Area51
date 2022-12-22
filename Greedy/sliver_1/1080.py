# 1080 : 행렬
# https://www.acmicpc.net/problem/1080

# 그냥 복잡한 문제일 뿐, 어려운 것 하나도 없음
import sys
n, m = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))

mtx1, mtx2 = [], []
for i in range(n):
    string = sys.stdin.readline().rstrip()
    temp = []
    for char in string:
        temp.append(int(char))
    mtx1.append(temp)
for i in range(n):
    string = sys.stdin.readline().rstrip()
    temp = []
    for char in string:
        temp.append(int(char))
    mtx2.append(temp)

# print(mtx1, mtx2)

count = 0
for i in range(0, n-2):
    for j in range(0, m-2):
        if mtx1[i][j] != mtx2[i][j]:
            count += 1

            for a in range(i, i+3):
                for b in range(j, j+3):
                    mtx1[a][b] = (mtx1[a][b] + 1) % 2

if mtx1 == mtx2:
    print(count)
else:
    print(-1)