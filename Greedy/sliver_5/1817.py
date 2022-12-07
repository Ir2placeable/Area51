# 1817 : 짐 챙기는 숌
# https://www.acmicpc.net/problem/1817

books, max_weight = map(lambda x: int(x), input().split(" "))
if books == 0:
    print(0)
else :
    box_weight_list = list(map(lambda x: int(x), input().split(" ")))
    boxes = 0
    now_weight = 0

    for box in box_weight_list:
        now_weight += box
        if now_weight == max_weight:
            boxes += 1
            now_weight = 0
        elif now_weight > max_weight:
            boxes += 1
            now_weight = box

    if not now_weight == 0:
        boxes += 1

    print(boxes)