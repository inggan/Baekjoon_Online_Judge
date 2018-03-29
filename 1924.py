N = input().split()

x = int(N[0])
y = int(N[1])
d = 0

def switch(day):
	return {
		1 : 'MON',
		2 : 'TUE',
		3 : 'WED',
		4 : 'THU',
		5 : 'FRI',
		6 : 'SAT',
		0 : 'SUN'
	}.get(day)
def switch2(month):
	return {
		1 : 31,
		2 : 28,
		3 : 31,
		4 : 30,
		5 : 31,
		6 : 30,
		7 : 31,
		8 : 31,
		9 : 30,
		10 : 31,
		11 : 30,
		12 : 31
	}.get(month)

for Repeat in range(1, x):
	if x != 1:
		d += switch2(Repeat	)
d += y	
print(switch(d%7))