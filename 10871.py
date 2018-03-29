num = input().split()
num2 = input().split()

N = int(num[0])
X = int(num[1])

for Repeat in range(0, N):
	if X > int(num2[Repeat]):
		print(num2[Repeat],end=" ")