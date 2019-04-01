N = int(input())
add = 0

for Rpt in range(0, N):
	Str = input().split('X')
	for rpt in range(0, len(Str)):
		for Rt in range(1, Str[rpt].count('O') + 1):
			add += Rt
	print(add)
	add = 0