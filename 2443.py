N = int(input())
minus = 1

for Repeat in range(0, N):
	for rep in range(0, Repeat):
		print(" ",end = "")
	for repeat in range(0, 2 * N - minus):
		print("*",end = "")
	minus += 2
	print("")