import sys

j = int(input())
for i in range(j):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)