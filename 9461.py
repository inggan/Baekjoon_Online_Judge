P = [0] * 100
P[0:5] = 1,1,1,2,2,3
T = int(input())

for rpt in range(6,100):
    P[rpt] = P[rpt - 1] + P[rpt - 5]

for Rpt in range(0,T):
    N = int(input())
    print(P[N - 1])