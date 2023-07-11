# 2872 : 우리집엔 도서관이 있어
# https://www.acmicpc.net/problem/2872
import sys

n = int(sys.stdin.readline())
books = []
for i in range(0, n):
    books.append(int(sys.stdin.readline()))

moves = 0
for i in range(n-1, -1, -1):
    if books[i] == n:
        n -= 1
    else:
        moves += 1

print(moves)