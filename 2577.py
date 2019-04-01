A = int(input())
B = int(input())
C = int(input())

num = A * B * C
num = list(map(int, str(num)))

for i in range(0, 10):
	print(num.count(i))