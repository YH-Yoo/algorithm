import heapq
import sys
input = sys.stdin.readline

N = int(input())
max_heap = []
for i in range(N):
	x = int(input())
	if x == 0:
		if not max_heap:
			print(0)
		else:
			print(-1 * (heapq.heappop(max_heap)))
	else:
		heapq.heappush(max_heap, -x)