import sys

arr = [0, 3, 7]
N = int(sys.stdin.readline())

for i in range(3, N + 1):
	arr.append(((arr[i - 2] * 3) + ((arr[i - 1] - arr[i - 2]) * 2)) % 9901)
print(arr[N])