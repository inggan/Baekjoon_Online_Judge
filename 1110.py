N = int(input())
M = N
repeat = 0

while N != M or repeat == 0:
	ddycle10 = N // 10
	ddycle1 = N % 10
	ddycle = (ddycle10 + ddycle1) % 10
	ddycle10 = ddycle1
	ddycle1 = ddycle
	N = ddycle10 * 10 + ddycle1
	repeat += 1
print(repeat)
