import sys

N = int(sys.stdin.readline())

stack = []
for i in range(0, N) :
	t = sys.stdin.readline().split()
	if t[0] == "push" :
		stack.append(t[1])
	if t[0] == "pop" :
		if (not stack) :
			print (-1)
		else :
			print(stack.pop())
	if t[0] == "size" :
		print(len(stack))
	if t[0] == "empty" :
		if len(stack) == 0:
			print(1)
		else :
			print(0)
	if t[0] == "top" :
		if len(stack) == 0:
			print(-1)
		else :
			print(stack[-1])
