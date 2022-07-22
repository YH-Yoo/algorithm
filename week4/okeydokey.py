import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
stack = []
count = 1
while num:
	if num and num[0] == count:
		count += 1
		num.pop(0)
	else:
		stack.append(num.pop(0))
	while stack:
		if stack[-1] == count:
			stack.pop()
			count += 1
		else:
			break

if not stack:
	print("Nice")
else:
	print("Sad")