from collections import deque
import sys

N = int(sys.stdin.readline())
d = deque()
for i in range(N):
	t = sys.stdin.readline().split()
	if t[0] == "push_front":
		d.appendleft(t[1])
	if t[0] == "push_back":
		d.append(t[1])
	if t[0] == "pop_front":
		if len(d) == 0:
			print (-1)
		else :
			print(d[0])
			d.popleft()
	if t[0] == "pop_back":
		if len(d) == 0:
			print (-1)
		else :
			print(d[-1])
			d.pop()
	if t[0] == "size":
		print(len(d))
	if t[0] == "empty":
		if len(d) == 0:
			print(1)
		else :
			print(0)
	if t[0] == "front":
		if d:
			print(d[0])
		else :
			print (-1)
	if t[0] == "back":
		if d:
			print(d[-1])
		else :
			print (-1)
