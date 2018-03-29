N = int(input())

lst = [0] * 41
lst[0:1] = [0,1]

def fibonacci(n):
	if n <= 1:
		return lst[n]
	else:
		if lst[n] == 0:
			lst[n] = fibonacci(n-1) + fibonacci(n - 2)
		return lst[n]

for repeat in range(0,N):
	p = int(input())

	if p == 0:
		print("1 0")
	else:
		print("%d %d"%(fibonacci(p-1),fibonacci(p)))