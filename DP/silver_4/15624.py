# 15624 : 피보나치 수 7
# https://www.acmicpc.net/problem/15624

n = int(input())
a, b = 0, 1

if n == 0:
    print(0)
if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    for _ in range(n):
        a, b = b, (a + b) % 1000000007
    print(a)
