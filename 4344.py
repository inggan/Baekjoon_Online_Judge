num = int(input())
sm = 0
ave = 0
num1 = 0

for Repeat in range(0, num):
	case = list(map(int,input().split()))
	for repeat in range(1, case[0]+1):
		sm += case[repeat]
	ave = sm / case[0]
	for rep in range(1, case[0]+1):
		if case[rep] > ave:
			num1 += 1
	result = num1 / case[0] * 100
	print("%.3f%%"%(result))
	sm = 0
	ave = 0
	num1 = 0