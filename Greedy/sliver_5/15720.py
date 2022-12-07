# 15720 : 카우버거
# https://www.acmicpc.net/problem/15720

a, b, c = map(lambda x: int(x), input().split(" "))

listA, listB, listC = [], [], []
original_cost, discount_cost = 0, 0

for i in range(0, 3):
    if i == 0:
        listA = list(map(lambda x: int(x), input().split(" ")))
    elif i == 1:
        listB = list(map(lambda x: int(x), input().split(" ")))
    else:
        listC = list(map(lambda x: int(x), input().split(" ")))

listA.sort(reverse=True)
listB.sort(reverse=True)
listC.sort(reverse=True)

for i in range(0, min(a,b,c)):
    temp_cost = listA.pop(0) + listB.pop(0) + listC.pop(0)
    original_cost += temp_cost
    discount_cost += temp_cost * 0.9

original_cost += sum(listA) + sum(listB) + sum(listC)
discount_cost += sum(listA) + sum(listB) + sum(listC)
print(original_cost)
print(int(discount_cost))