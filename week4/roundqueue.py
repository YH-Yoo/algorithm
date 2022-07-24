from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
q = deque(i for i in range(1, N + 1))
num = list(map(int, input().split()))

count = 0
for n in num:
	while 1:
		if q[0] == num:
			q.popleft()
			break
		else:
			if q.index(n) < len(q) // 2:
				q.rotate(-1)
				count += 1
			else :
				q.rotate(1)
				count += 1

print(count)