import sys

bracket = sys.stdin.readline().strip()

stack = []

for i in bracket:
	if i == '(':
		stack.append(i)
	elif i == ')':
		if stack and stack[-1] == '(':
			stack.pop()
		else:
			stack.append(i)
print(len(stack))