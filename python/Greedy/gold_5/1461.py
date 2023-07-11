# 1461 : 도서관
# https://www.acmicpc.net/problem/1461

# 책을 들고 갈 수 있는 수만큼 책을 겹친다 -> 겹쳐진 책은 한번에 이동된다.
# 부호가 다르면 둘로 나눈다.
# 절댓값이 가장 큰 수는 1번 더하고, 나머지 수는 2번씩 더한다.
import sys

books, carry = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
locations = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))
locations.sort()

index = len(locations)
for i in range(0, books):
    if locations[i] > 0:
        index = i
        break


temp1 = locations[:index]
temp2 = locations[index:]
# print(temp1, temp2)

new_locations = []
index = 0
while index < len(temp1):
    new_locations.append(temp1[index] * -1)
    index += carry
index = len(temp2)-1
while index > -1:
    new_locations.append(temp2[index])
    index -= carry
new_locations.sort()
# print(new_locations)

step = new_locations.pop()
step += sum(new_locations) * 2

print(step)