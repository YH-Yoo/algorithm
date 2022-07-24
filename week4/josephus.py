from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
dq = deque(i for i in range(1, N + 1))
res = []

for i in range(N):
	dq.rotate(-(K - 1))
	res.append(dq.popleft())

print("<", ", ".join(str(i) for i in res), ">", sep = '')