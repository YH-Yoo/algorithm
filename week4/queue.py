from collections import deque
import sys

N = int(sys.stdin.readline())
que = []
for i in range(N):
	t = sys.stdin.readline().split()
	if t[0] == "push":
		que.append(t[1])
	if t[0] == "pop":
		if que :
			print(que.pop(0))
		else :
			print(-1)
	if t[0] == "size":
		print(len(que))
	if t[0] == "empty":
		if not que:
			print(1)
		else :
			print(0)
	if t[0] == "front":
		if que:
			print(que[0])
		else :
			print(-1)
	if t[0] == "back":
		if que:
			print(que[-1])
		else :
			print(-1)
