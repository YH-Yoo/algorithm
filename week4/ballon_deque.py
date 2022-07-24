import collections


from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dq = deque(enumerate(map(int, input().split())))
arr = []

while dq:
	index, paper = dq.popleft()
	arr.append(index + 1)
	if paper > 0:
		dq.rotate(-(paper - 1))
	else:
		dq.rotate(-paper)
print(' '.join(map(str, arr)))