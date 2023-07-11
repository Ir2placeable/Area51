# https://www.acmicpc.net/problem/20055

# 문제의 내용이 매우 많다 -> 구현, 시뮬레이션 문제이다.
# 구현, 시뮬레이션 문제는, 변수 이름을 잘 정해서 이해가 쉽도록 해야한다.
# 구현, 시뮬레이션 문제는, 문제 조건을 잘 정리해야 한다.
# 이 문제는 실제로 삼성 코테 문제이다.

# 1 ~ N : 올리는 위치 -> 로봇이 올라갈 수 있음
# N+1 ~ 2N : 내리는 위치 -> 로봇 도달시 즉시 내림 -> 벨트는 1~N 까지만 필요함
# 로봇이 올라가거나, 특정 위치로 이동하면 해당 위치의 내구도 1 감소

import sys
from collections import deque

length, end_condition = map(lambda x: int(x), sys.stdin.readline().split())
durability = deque(map(lambda x: int(x), sys.stdin.readline().split()))
robot = deque([0 for _ in range(length)])

current_state = 0
# 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
while durability.count(0) < end_condition:
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    robot.rotate(1)
    durability.rotate(1)
    robot[-1] = 0
    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    for i in range(length-2, -1, -1):
        if robot[i] == 0:
            continue
        if robot[i+1] == 1:
            continue
        if durability[i+1] == 0:
            continue

        robot[i] = 0
        robot[i+1] = 1
        durability[i+1] -= 1
    # 벨트 마지막 자리에는 로봇이 있으면 움직여서 0 이 되고, 로봇이 없으면 애초에 0 이다.
    robot[-1] = 0
    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if durability[0] != 0 and robot[0] == 0:
        robot[0] = 1
        durability[0] -= 1

    current_state += 1

print(current_state)