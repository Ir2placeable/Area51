# 15624 : 피보나치 수 7
# https://www.acmicpc.net/problem/15624

n = int(input())

a = 0
b = 1

if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    for _ in range(n):
        a, b = b % 1000000007, (a + b) % 1000000007

    print(a)