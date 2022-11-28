# 9237 : 이장님 초대
# https://www.acmicpc.net/problem/9237

# 마지막 나무가 다 자란 다음날 이장님을 초대할 것이다

tree_count = int(input())
tree_list = list(map(lambda ele: int(ele), input().split(" ")))
tree_list.sort(reverse=True)

for i in range(0, len(tree_list)):
    tree_list[i] += i+1

print(max(tree_list) + 1)