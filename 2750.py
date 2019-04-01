N = int(input())
lst = []

for rpt in range(0, N):
	lst.append(int(input()))

lst.sort()

for Rpt in range(0, N):
	print(lst[Rpt])