# 16953 : A -> B
# https://www.acmicpc.net/problem/16953

a, b = map(lambda x: int(x), input().split(" "))

tasks = 0
while a < b:
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 1:
        break
    else:
        b //= 2
    tasks += 1

if a == b:
    print(tasks + 1)
else:
    print(-1)
