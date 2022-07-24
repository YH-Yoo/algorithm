import heapq
import sys
input = sys.stdin.readline

heap = []
N = int(input())
for i in range(N):
	arr = list(map(int, input().split()))
	while arr:
		if len(heap) < N:
			heapq.heappush(heap, arr.pop())
		else :
			if heap[0] < arr[0]:
				heapq.heappop(heap)
				heapq.heappush(heap, arr.pop())

print(heap[0])