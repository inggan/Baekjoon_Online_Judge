N = int(input())
ddycle = 0

while True:
	if N % 5 == 0:
		print(N//5+ddycle)
		break
	elif N < 0:
		print("-1")
		break
	ddycle += 1
	N -= 3