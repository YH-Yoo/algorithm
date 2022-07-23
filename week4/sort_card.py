import heapq
import sys
N = int(sys.stdin.readline())
min_heap = []
res = 0
for i in range(N):
	heapq.heappush(min_heap, int(sys.stdin.readline()))
if len(min_heap) == 1:
	print(0)
else:
	while 1 < len(min_heap) :
		res += heapq.heappop(min_heap) + heapq.heappop(min_heap)
		heapq.heappush(min_heap, res)
	print(res)


# 이건 왜 되지???????????????????????/
# https://velog.io/@dding_ji/baekjoon-17150919