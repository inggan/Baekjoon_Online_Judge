import sys

T = sys.stdin.readline()

for Repeat in range(0, int(T)):
	num = sys.stdin.readline().split()
	num1 = int(num[0])
	num2 = int(num[1])
	print(num1 + num2)