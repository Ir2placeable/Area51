# 5639 : 이진 검색 트리
# https://www.acmicpc.net/problem/5639
import sys
sys.setrecursionlimit(10**6)

preOrder = []
while True:
    try:
        preOrder.append(int(input()))
    except:
        break


def postOrder(start_index, end_index):
    if start_index > end_index:
        return

    # 왼쪽 노드와 오른쪽 노드를 구분하는 divide_index 를 만들 것이다.
    # 이때, divide_index 는 end_index + 1 으로 초기화 하는 이유는, 오른쪽에 노드가 없는 경우를 의미한다.
    # 루트 기준으로 작은 값들은 왼쪽 노드 / 큰 값들은 오른쪽 노드에 위치한다.
    divide_index = end_index + 1
    for i in range(start_index + 1, end_index + 1):
        if preOrder[i] > preOrder[start_index]:
            divide_index = i
            break

    # 왼쪽 노드 재귀
    postOrder(start_index + 1, divide_index - 1)
    # 오른쪽 노드 재귀
    postOrder(divide_index, end_index)
    print(preOrder[start_index])


postOrder(0, len(preOrder) - 1)
