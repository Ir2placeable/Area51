# 1026 : 보물
# https://www.acmicpc.net/problem/1026

# A 재배열, B 고정

N = int(input())
A = list(map(lambda x: int(x), input().split(" ")))
B = list(map(lambda x: int(x), input().split(" ")))
A.sort()
B.sort(reverse=True)

acc = 0
for i in range(0, N):
    acc += A[i] * B[i]

print(acc)
