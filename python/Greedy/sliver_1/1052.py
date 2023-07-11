# 1052 : 물병
# https://www.acmicpc.net/problem/1052

# n의 값을 1,2,4,8 형태의 조합으로 만든 후에, 그 개수가 k개를 넘지 않도록 한다.
# ex) 13 2 -> [8, 4, 1] 조합으로 만든다. -> k=2 이므로 해당 리스트의 길이가 2가 되어야 한다.
# 리스트를 2개 팝하고 그 차이를 bottles 로 기록한다.
import sys

n, k = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))

list2 = []
i2 = 1
while i2 <= n:
    list2.append(i2)
    i2 *= 2

list3 = []
while n > 0:
    temp = list2.pop()
    if n >= temp:
        list3.append(temp)
        n -= temp

bottles = 0
while len(list3) > k:
    a = list3.pop()
    b = list3.pop()
    bottles += b - a
    list3.append(2*b)

print(bottles)