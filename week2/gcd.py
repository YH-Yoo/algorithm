import sys
import math

t = int(sys.stdin.readline())
for i in range(t):
	arr = list(map(int, sys.stdin.readline().split()))
	sum = 0
	for j in range(1, len(arr)):
		for k in range(j + 1, len(arr)):
			sum += math.gcd(arr[j], arr[k])
	print(sum)
