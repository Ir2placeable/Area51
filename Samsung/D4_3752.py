# 조합 문제
# N : 최대 100

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    numbers = list(map(lambda x: int(x), input().split()))

    length = sum(numbers) + 1
    scores = [0 for _ in range(length+1)]
    scores[0] = 1

    while numbers:
        score = numbers.pop()
        next_scores = scores[:]

        for i in range(length-1, -1, -1):
            if scores[i] == 1 and i + score < length:
                next_scores[i + score] = 1

        scores = next_scores

    result = sum(scores)
    print("#%d %d" % (test_case, result))
