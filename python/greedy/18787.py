# 18787 : Mad Scientist
# https://www.acmicpc.net/problem/18787

N = int(input())
A = input()
B = input()

change_index = []
for i in range(0, N):
    if A[i] != B[i]:
        change_index.append(i)

count = 0
prev = -2
for index in change_index:
    count += 1
    if prev + 1 == index:
        count -= 1
    prev = index

print(count)