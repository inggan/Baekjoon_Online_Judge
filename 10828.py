J = int(input())

stack = []

for a in range(J):
	N = input().split()
	if N[0] == "push":
		stack.append(int(N[1]))
	elif N[0] == "pop":
		try:
			print(stack.pop())
		except:
			print(-1)
			continue
	elif N[0] == "size":
		print(len(stack)) 
	elif N[0] == "empty":
		if len(stack) == 0:
			print(1)
		else:
			print(0)
	elif N[0] == "top":
		if len(stack) == 0:
			print(-1)
			continue
		print(stack[-1])