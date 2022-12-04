# 2839 : 설탕 배달
# https://www.acmicpc.net/problem/2839

# 경우의 수를 전부 구해보는 것이다..!

sugar = int(input())
bags = []

for i5 in range(0, sugar//5 + 1):
    for i3 in range(0, sugar//3 + 1):
        if i3*3 + i5*5 == sugar:
            bags.append(i3+i5)

if len(bags) == 0:
    print(-1)
else:
    print(bags[-1])