num = []

def selfnum(num):
	sub = num
	if num >= 10000:
		sub += num // 10000
		num %= 10000
	if num >= 1000:
		sub += num // 1000
		num %= 1000 
	if num >= 100:
		sub += num // 100
		num %= 100
	if num >= 10:
		sub += num // 10
		num %= 10  
	sub += num
	return sub
for Repeat in range(1, 10001):
	num.append(selfnum(Repeat))
for repeat in range(1, 10001):
	if num.count(repeat) == 0:
		print(repeat)-+