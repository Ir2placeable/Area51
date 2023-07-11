# 2697 : 다음수 구하기
# https://www.acmicpc.net/problem/2697

import sys
test_case = int(sys.stdin.readline())

for i in range(test_case):
    string = sys.stdin.readline().rstrip()
    items = []
    for char in string:
        items.append(char)

    pivot = len(items)
    for j in range(len(items)-1, 0, -1):
        pivot = j
        if items[j-1] < items[j]:
            break

    a = items[:pivot]
    b = items[pivot:]
    temp = a.pop()
    b.sort()
    for j in range(0, len(b)):
        if temp < b[j]:
            a.append(b.pop(j))
            b.insert(j, temp)
            break

    if len(a) == 0:
        print('BIGGEST')
        continue
    a = a+b
    result = ''
    for k in a:
        result += k
    print(result)



# 2 7 9 1 3 4 3 9 9 7 4 2
# 2 7 9 1 3 4 4 2 3 7 9 9

