S = input()

for Rpt in range(0, 26):
	print(str(S.find(chr(ord('a') + Rpt))) + " ",end="")