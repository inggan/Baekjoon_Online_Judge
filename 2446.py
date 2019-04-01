N = int(input())
minus = 1

for Repeat in range(0, 2 * N - 1):
	if 2 * N - Repeat > N:
		for repeat in range(0, Repeat):
			print(" ", end = "")
		for Rpt in range(0, 2 * N - minus):
			print("*", end = "")
		minus += 2
		if Repeat == N - 1:
			minus -= 4
	else:
		for repeat in range(0, 2 * N - Repeat - 2):
			print(" ", end = "")
		for Rpt in range(0, 2 * N - minus):
			print("*", end = "")
		minus -= 2
	print("")