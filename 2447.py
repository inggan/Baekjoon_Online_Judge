N = 9

lst = [[0] * N for i in range(N)]

def makestar(n):

	star = N // 3
	cnt = 1

	if N == 1:
		lst[0][0] = 1
		return
	else:
		for RPT in range(0, n, 3):
			for rpt in range(0, n, 3):
				lst[RPT][rpt], lst[RPT][rpt + 1] , lst[RPT][rpt + 2] = 1, 1, 1
				lst[RPT + 1][rpt], lst[RPT + 1][rpt + 2] = 1, 1
				lst[RPT + 2][rpt], lst[RPT + 2][rpt + 1] , lst[RPT + 2][rpt + 2] = 1, 1, 1
makestar(N)

for Repeat in range(0, N):
	for repeat in range(0, N):
		if lst[Repeat][repeat] == 1:
			print("*", end = "")
		else:
			print(" ", end = "")
	print("")