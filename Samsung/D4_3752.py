test_case = int(input())
for case_number in range(1, test_case + 1):
    n = int(input())
    scores = list(map(lambda x: int(x), input().split()))

    total_score = sum(scores)
    score_cases = [0 for _ in range(total_score + 1)]
    score_cases[0] = 1

    for score in scores:
        for i in range(total_score, -1, -1):
            if score_cases[i] == 1 and i + score <= total_score:
                score_cases[i + score] = 1

    result = sum(score_cases)
    print("#%d %d" % (case_number, result))