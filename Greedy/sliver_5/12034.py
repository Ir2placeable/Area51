# 12034 : 김인천씨의 식료품가게(Large)
# https://www.acmicpc.net/problem/12034

# 식품은 4의 배수
# 할인 가격 0.75는 정수

test_case = int(input())

for i in range(1, test_case+1):
    items = int(input())
    item_list = list(map(lambda x: int(x), input().split(" ")))

    discount_list = []

    for j in range(0, items):
        target = int(item_list.pop() * 0.75)
        item_list.remove(target)
        discount_list.insert(0, target)

    format_string = ''
    for j in range(0, items-1):
        format_string += str(discount_list[j]) + ' '
    format_string += str(discount_list[-1])

    print('Case #%i: %s' %(i, format_string))