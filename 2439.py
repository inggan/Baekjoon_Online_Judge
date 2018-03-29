N = int(input())

for Repeat in range(1, N+1):
	for repeat in range(Repeat, N):
		print(" ",end="")
	for rep in range(0, Repeat):
		print("*",end="")
	print("")