N = int(input())
minus = 2

for Repeat in range(1, N * 2):
	if N - Repeat >= 0:
		for repeat in range(0, Repeat):
			print("*", end = "")
		for Rpt in range(0, N * 2 - minus):
			print(" ", end = "") 
		for rpt in range(0, Repeat):
			print("*", end = "")
		minus += 2
		if N - Repeat == 0:
			minus -= 4
	else:
		for repeat in range(0, 2 * N -Repeat):
			print("*", end = "")
		for Rpt in range(0, N * 2 - minus):
			print(" ", end = "")
		for rpt in range(2 * N - Repeat, 0, -1):
			print("*", end = "")
		minus -= 2 
	print("")