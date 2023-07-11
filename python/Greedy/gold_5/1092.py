# 1092 : 크레인
# https://www.acmicpc.net/problem/1092

# 크레인의 작동 최소 시간을 구해야한다. -> 그리디 알고리즘인 것 파악 가능
# 크레인이 최소한으로 작동하려면 리미트가 가장 높은 크레인이 가장 큰 무게를 들어야 한다. -> 정렬
import sys

cranes = int(sys.stdin.readline())
crane_list = sorted(list(map(lambda x: int(x), sys.stdin.readline().split())), reverse=True)
boxes = int(sys.stdin.readline())
box_list = sorted(list(map(lambda x: int(x), sys.stdin.readline().split())), reverse=True)

if crane_list[0] < box_list[0]:
    print(-1)
else:
    time = 0
    while len(box_list) > 0:
        for crane in crane_list:
            for box in box_list:
                if crane >= box:
                    box_list.remove(box)
                    break
        time += 1
    print(time)