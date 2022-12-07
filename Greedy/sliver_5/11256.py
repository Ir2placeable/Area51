# 11256 : 사탕
# https://www.acmicpc.net/problem/11256

test_case = int(input())

for i in range(0, test_case):
    num_of_used_box = 0
    num_of_candy, num_of_boxes = map(lambda x: int(x), input().split(" "))

    list_of_capacity = []
    for j in range(0, num_of_boxes):
        a, b = map(lambda x: int(x), input().split(" "))
        list_of_capacity.append(a * b)

    list_of_capacity.sort(reverse=True)

    for capacity in list_of_capacity:
        num_of_candy -= capacity
        num_of_used_box += 1
        if num_of_candy <= 0:
            break

    print(num_of_used_box)