N = int(input())

for i in range(2 , N + 1):
	if N == 1:
		break
	while not N % i:
		print(i, sep="\n")
		N //= i