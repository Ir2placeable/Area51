# 13164 : 행복 유치원
# https://www.acmicpc.net/problem/13164

# 이전 푼 문제중, 고속도로에 전파소를 설치하는 문제와 동일하다.
# 키 차이가 큰 아이만 따로 빼서 하나의 그룹으로 만들어버린다.
# 1 3 5 6 10 인 경우, 6과 10의 차이가 가장 크므로 10을 따로 뺀다. -> 남은 아이들은 1 3 5 6
# 1과 3의 차이가 크므로 1을 따로 뺀다 -> 3 5 6 이 1개의 그룹이다. 3-5 + 5-6을 구하면 된다.

# 쉽게 하는 방법은 아이들의 키 차이를 구한 후, 정렬한다. 이 중 남은 아이들의 수의 sum을 구하면 된다.
# 두 명을 제외시켰으므로 3명의 sum을 구한다.
import sys

n, k = map(lambda x: int(x), sys.stdin.readline().rstrip().split(" "))
students = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(" ")))

diff_list = []
for i in range(0, n-1):
    diff_list.append(students[i+1] - students[i])
diff_list.sort()

print(sum(diff_list[:n-k]))
# print(diff_list)