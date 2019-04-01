N = int(input())
minus = 2

for Repeat in range(1, 2 * N):
	if N - Repeat >= 0:
		for repeat in range(Repeat, N):
			print(" ", end = "")
		for rep in range(0, 2 * Repeat - 1):
			print("*", end = "")
	else:
		for Rpt in range(0, -(N - Repeat)):
			print(" ", end = "")
		for rpt in range(1, 2 * N - minus):
			print("*", end = "")
		minus += 2
	print("")