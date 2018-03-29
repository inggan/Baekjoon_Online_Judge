num = int(input())
score = list(map(int,input().split()))
mx = max(score)
ave = 0

for Repeat in range(0, num):
	score[Repeat] = score[Repeat] / mx * 100
	ave += score[Repeat]
print("%.2f" %(ave/num))	