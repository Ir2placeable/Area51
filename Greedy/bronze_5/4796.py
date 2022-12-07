# 4796 : 캠핑
# https://www.acmicpc.net/problem/4796

case = 0
while 1:
    case += 1

    l, p, v = map(lambda x: int(x), input().split(" "))
    if l == 0:
        break

    cycle = v//p

    print_line = 'Case %d: %d' % (case, l * cycle + min(l, v%p))
    print(print_line)