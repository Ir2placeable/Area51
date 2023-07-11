# 12970 : AB
# https://www.acmicpc.net/problem/12970

# 수학적으로 계산해야 하는 문제

n, k = map(lambda x: int(x), input().split(" "))

max_k = n//2 * (n - n//2)
# print(max_k)

if k > max_k:
    print(-1)
else:
    if k == 0:
        print('B' * n)
    else:
        a = 0
        b = n
        while a * b < k and b > 0:
            a += 1
            b -= 1
        a -= 1
        b += 1
        remain = k - a*b + a
        # print(a, b, remain)

        p1 = 'A' * a
        p2 = 'B' * (n - a - 1 - remain)
        p3 = 'A'
        p4 = 'B' * remain
        print(p1 + p2 + p3 + p4)