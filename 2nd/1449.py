# 문제 첫 인상 : 단순 계산 문제로 보임.
# 구멍난 위치를 메꾸기 위해서는, 양 옆 0.5cm를 추가로 메워야 함.
# -> 테이프 하나의 길이와, 그 테이프가 커버할 수 있는 영역의 차이가 발생함. -> 테이프가 커버할 수 있는 영역을 우선 계산
# 구멍난 위치가 무작위로 들어오기 때문에 정렬함. (구멍의 개수가 1000개 미만이라 정렬하는데 문제 없음. cf) 100,000개 이하만 정렬가능)
# 일단 첫 구멍을 테이프 하나로 메꾸고, 테이프의 길이가 다음 구멍까지 커버할 수 있는지 체크!
# -> 이때, 다다음, 다다다음 구멍까지 커버하는 경우 있으니 while로 체크
# for 문은 index의 값을 내맘대로 수정할 수 없기 때문에, while문을 사용함.

import sys

n, tape_length = map(lambda x: int(x), sys.stdin.readline().split())
leakage = list(map(lambda x: int(x), sys.stdin.readline().split()))

leakage.sort(reverse=True)
coverage = tape_length - 1
result = 0

while leakage:
    single_leakage = leakage.pop()
    result += 1

    while leakage and single_leakage + coverage >= leakage[-1]:
        leakage.pop()

print(result)
