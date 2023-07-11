# 9440 : 숫자 더하기
# https://www.acmicpc.net/problem/9440

while True:
    items = list(input().split(" "))
    if len(items) == 1:
        break
    items.pop(0)
    items.sort()

    count = 0
    while items[0] == '0':
        items.pop(0)
        count += 1
    while count > 0:
        items.insert(2, '0')
        count -= 1

    a = ''
    b = ''
    for i in range(0, len(items)):
        if i % 2 == 0:
            a += items[i]
        else:
            b += items[i]
    print(int(a) + int(b))
