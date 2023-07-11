# 3213 : 피자
# https://www.acmicpc.net/problem/3213

n = int(input())
rest = []

for i in range(0, n):
    a = input()
    if a == '1/4':
        a = 1
    elif a == '1/2':
        a = 2
    else:
        a = 3
    rest.append(a)
rest.sort(reverse=True)

result = 0
while len(rest) != 0:
    result += 1
    piece = rest.pop(0)

    if piece == 3:
        if 1 in rest:
            rest.pop(rest.index(1))
    elif piece == 2:
        if 2 in rest:
            rest.pop(rest.index(2))
        else:
            temp = 0
            while temp < 2 and 1 in rest:
                rest.pop(rest.index(1))
                temp += 1
    else:
        temp = 0
        while temp < 4 and 1 in rest:
            rest.pop(rest.index(1))
            temp += 1

print(result)