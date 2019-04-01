N = int(input())
words = set()

for rpt in range(0,N):
    words.add(input())
for rpt in sorted(words,key=lambda x:(len(x),x)):
    print(rpt)