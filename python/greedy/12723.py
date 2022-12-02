# 12723 : Minimum Scalar Product (Small)
# https://www.acmicpc.net/problem/12723

test_case = int(input())

for i in range(1, test_case + 1):
    result = 0
    n = int(input())
    v1 = list(map(lambda x: int(x), input().split(" ")))
    # 작은 순
    v1.sort()
    v2 = list(map(lambda x: int(x), input().split(" ")))
    # 큰 순
    v2.sort(reverse=True)

    for j in range(0, n):
        result += v1[j] * v2[j]

    print('Case #%i: %i' % (i, result))