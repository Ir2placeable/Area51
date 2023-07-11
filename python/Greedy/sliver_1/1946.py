# 1946 : 신입 사원
# https://www.acmicpc.net/problem/1946

# 2초에 N <= 100,000. 따라서 N^2 불가능
# 1차 시도 : 서류 심사 결과 정렬-> 가장 강한 지원자가 나온다.
# 가장 강한 지원자를 기준으로 조건을 판별한다.
# 만약 다음 지원자가 조건을 통과한다면, 강한 지원자로 선택한다.

import sys

test_case = int(sys.stdin.readline())
for i in range(test_case):
    n = int(sys.stdin.readline())

    people = []
    for j in range(n):
        people.append(list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))))
    people = sorted(people, key=lambda x: x[0])

    winner = 1
    a = people[0]
    for j in range(1, n):
        b = people[j]

        if a[1] > b[1]:
            winner += 1
            a = b

    print(winner)