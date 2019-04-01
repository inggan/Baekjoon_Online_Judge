num = int(input())

for Repeat in range(1, num + 1):
	for repeat in range(num, Repeat, -1):
		print(" ", end = "")
	for rep in range(0, 2 * Repeat - 1):
		print("*", end = "")
	print("")