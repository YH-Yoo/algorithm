import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(N - 2):
	for j in range(i + 1, N - 1):
		for k in range(j + 1, N):
			if lst[i] + lst[j] + lst[k] > M:
				continue
			else:
				result = max(result,  lst[i] + lst[j] + lst[k])
print(result)