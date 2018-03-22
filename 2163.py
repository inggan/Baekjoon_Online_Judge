inp = input().split()

N = int(inp[0])
M = int(inp[1])


if(1<=N or M<=300):

	X = (N-1) + N * (M-1)

	print(X)