lst = [0,0]

N = int(input())

for rpt in range(2, N + 1):
	lst.append(lst[rpt-1]+1)
	if rpt % 2 == 0:
		lst[rpt] = min(lst[rpt], lst[rpt//2]+1)
	if rpt % 3 == 0:
		lst[rpt] = min(lst[rpt], lst[rpt//3]+1)
print(lst[N])