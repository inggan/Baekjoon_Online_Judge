import math

N = int(input())
num = input().split()
repeat = 2

num = [int (i) for i in num]
num.sort()
num.reverse()
mx = num[0]

root = math.sqrt(mx)

if num.count(1):
	num.insert(num.index(1), 0) 
	num.remove(1)
for Repeat in range(2, int(root+1)):
	while Repeat * repeat <= mx:
		if num.count(Repeat * repeat):
			num.insert(num.index(Repeat * repeat), 0) 
			num.remove(Repeat * repeat)
		repeat += 1
	repeat = 2
print(N-num.count(0))