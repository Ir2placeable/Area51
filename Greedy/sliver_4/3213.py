# 3213 : 피자
# https://www.acmicpc.net/problem/3213
import math

n = int(input())
restofem = []

result = 0
for i in range(0, n):
    a = input()
    if a in restofem:
        restofem.pop(restofem.index(a))
        continue

    result += 1
    if a == '1/4':
        restofem.append('3/4')
    elif a == '1/2':
        restofem.append('1/2')
    else:
        restofem.append('1/4')

print(result)