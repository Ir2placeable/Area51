# 21316 : 스피카
# https://www.acmicpc.net/problem/21316

# 스피카의 특징
# 스피카로 이어진 점 a : 3개의 선분을 가진다.
# 스피카로 이어진 점 b : 2개의 선분을 가진다.
# 스피카로 이어진 점 c : 1개의 선분을 가진다.

cases = [[] for _ in range(13)]
for _ in range(12):
    a, b = map(lambda x: int(x), input().split(" "))
    cases[a].append(b)
    cases[b].append(a)

for i in range(1, 13):
    if len(cases[i]) != 3:
        continue

    connected = 0
    for j in range(3):
        connected += len(cases[cases[i][j]])

    if connected == 6:
        print(i)
        break