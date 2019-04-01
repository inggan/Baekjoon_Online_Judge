X = int(input())
stick = 64
cnt = 0

while X>0:
	if not X - stick < 0:
		X -= stick
		cnt+=1
	else:
		stick//=2
		
print(cnt)