# 10826 : 피보나치 수 4
# https://www.acmicpc.net/problem/10826

a, b = 0, 1
k = int(input())

while k > 0:
    a, b = b, a+b
    k -= 1

print(a)