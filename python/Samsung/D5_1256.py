import heapq

test_case = int(input())
for case_number in range(1, test_case + 1):
    target = int(input())

    string = list(input())
    substrings = []

    prev = ''
    while string:
        prev = string.pop() + prev
        heapq.heappush(substrings, prev)

    result = ''
    for i in range(target):
        result = heapq.heappop(substrings)

    print("#%d %s" % (case_number, result))