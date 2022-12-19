# 15889 : 호 안에 수류탄이야!!
# https://www.acmicpc.net/problem/15889
import sys

n = int(sys.stdin.readline())
positions = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
if n == 1:
    print('권병장님, 중대장님이 찾으십니다')
else:
    ranges = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))

    max_range = 0
    flag = True
    for i in range(0, n-1):
        max_range = max(max_range, positions[i] + ranges[i])
        if max_range >= positions[i+1]:
            continue
        else:
            flag = False
            break

    if flag:
        print('권병장님, 중대장님이 찾으십니다')
    else:
        print('엄마 나 전역 늦어질 것 같아')