N = int(input())

for Repeat in range(0, N):
	for repeat in range(0,Repeat):
		print(" ",end="")
	for repeat2 in range(0, N-Repeat):
		print("*",end="")
	print("")