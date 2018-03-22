num = input().split()
	
N = int(num[0])
L = int(num[1])

def sequencesum(N, L):
	if L <= 100 and N <= 1000000000:
		global t
		global d
		t = 0
		d = 0
		for repeat in range(1, L):
			t += repeat
		x = (N - t) // L
		if x < 0:
			sequencesum(N, L + 1)
		else:
			for repeat in range(0, L):
				d += x + repeat 
			if d > N or d < N:
				sequencesum(N, L + 1)
			elif d == N:
				for repeat in range(0, L):
					print(x+repeat,end=" ")
	else:
		print("-1")

sequencesum(N, L)		