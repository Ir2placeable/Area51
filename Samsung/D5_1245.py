# 구현

t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    temp = list(map(lambda x: int(x), input().split()))

    locations = temp[:n]
    scales = temp[n:]

    default_F = 0
    for i in range()