import math

num = input().split()

mini = int(num[0])
maxi = int(num[1])
cnt = 0
nono = 0
lst = list()

while True:
	if nono**2 > maxi:
		break
	lst.append(nono**2)
	nono += 1

for rpt in range(mini, maxi + 1):
	if rpt 

print(cnt)	