# 9009 : 피보나치
# https://www.acmicpc.net/problem/9009

# 정수 n은 서로 다른 피보나치수f 로 표현된다. 이때, f의 최소 개수를 이용하자.
# n 까지 피보나치 수를 구해서 리스트를 만든 다음. 그 리스트 역순 정렬하고 앞에서부터 꺼내 쓴다.
# 이렇게 하면, 어떤 피보나치 수를 써야 하는지만 알면 된다.

import sys

n = int(sys.stdin.readline())
for i in range(n):
    a = int(sys.stdin.readline())
    pivo = [0, 1]

    while True:
        num = pivo[-1] + pivo[-2]
        if num > a:
            break

        pivo.append(num)

    used = []
    while a > 0:
        temp = pivo.pop()
        if temp <= a:
            a -= temp
            used.append(temp)

    result = ''
    for k in used:
        result = str(k) + ' ' + result

    print(result[:-1])