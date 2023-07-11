# https://www.acmicpc.net/problem/19583

# 출석 기준
# 1. 개강총회 시작 이전에 채팅 기록이 있는 사람
# 2. 개강총회 종료 ~ 스트리밍 종료에 채팅 기록이 있는 사람
# 1, 2번을 만족해야 출석이 인정된다.

import sys
start, end, terminate = map(lambda x: int(x[:2]) * 100 + int(x[3:]), sys.stdin.readline().split())

visitor = set()
count = 0
while True:
    temp = sys.stdin.readline()
    if len(temp) < 3:
        break

    time, name = temp.split()
    time = int(time[:2] + time[3:])

    if time <= start:
        visitor.add(name)
    elif end <= time <= terminate and name in visitor:
        visitor.discard(name)
        count += 1
print(count)