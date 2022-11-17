# 10162 : 전자레인지
# https://www.acmicpc.net/problem/10162

# A 버튼 : 5분 == 300초
# B 버튼 : 1분 == 60초
# C 버튼 : 10초
# A, B, C 버튼을 최소 횟수로 누르는 경우를 찾아야 함
# 이때, 최소 횟수 -> 그리디 알고리즘 사용

# 일단, 제일 먼저 생각나는 방식은, C 버튼으로만 답을 찾는 것.
# 그리고 C버튼 6번 == B버튼 1번 임을 이용하여, 답을 줄여 나가는 것이다.

target_time = int(input())

# 답이 없는 경우
if target_time % 10 != 0:
    print(-1)

# 답이 있는 경우
else:
    buttonA, buttonB, buttonC = 0, 0, 0

    buttonC = target_time // 10

    buttonB = buttonC // 6
    buttonC = buttonC % 6

    buttonA = buttonB // 5
    buttonB = buttonB % 5

    print(buttonA, buttonB, buttonC)
