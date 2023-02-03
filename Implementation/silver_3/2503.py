# https://www.acmicpc.net/problem/2503

# 구현 문제는 꼼꼼히 읽어보고 천천히 구현한다.
# 2번 이상 문제를 다시 읽으면 실패다!

# 1 ~ 9 로 세자리 수를 만들 수 있는 경우 -> 94
# 최대 질문 개수 -> 100
# 최대 약 10000회 연산 -> 완전 탐색 가능

import sys, itertools

n = int(sys.stdin.readline())
questions = []
for _ in range(n):
    num, strike, ball = sys.stdin.readline().split()
    questions.append([list(num), int(strike), int(ball)])
# print(questions)

cases = set(itertools.permutations([str(i) for i in range(1, 10)], 3))
for case in cases.copy():
    for target_case, target_strike, target_ball in questions:
        strike, ball = 0, 0

        for i in range(3):
            if case[i] == target_case[i]:
                strike += 1
            elif case[i] in target_case:
                ball += 1

        if target_strike != strike or target_ball != ball:
            cases.discard(case)

print(len(cases))