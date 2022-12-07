# 17262 : 팬덤이 넘쳐흘러
# https://www.acmicpc.net/problem/17262

fans = int(input())
times = []

for i in range(0, fans):
    times.append(list(map(lambda x: int(x), input().split(" "))))

listA = sorted(times, key=lambda x: x[1])
listB = sorted(times, key=lambda x: x[0], reverse=True)

diff = listB[0][0] - listA[0][1]

if diff <= 0 :
    print(0)
else:
    print(diff)