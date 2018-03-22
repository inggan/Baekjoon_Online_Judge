n = int(input())
sequencestr = input().split()
sequence = list(range(n))

for repeat in range(0, n):
	sequence[repeat] = int(sequencestr[repeat])

class cs:
	def msa(self, num, n):
		sm = num[0]
		result = num[0]

		for repeat in range(1, n):
			sm = max(sm + num[repeat], num[repeat])
			result = max(sm, result)

		return result

mx = cs()
print(mx.msa(sequence, n))