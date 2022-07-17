import heapq
import sys
input = sys.stdin.readline

max_heap = []
for i in range(N):
	x = int(input())
	if not max_heap:
		print(0)
	else: