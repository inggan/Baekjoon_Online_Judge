DP = [0] * 11
DP[0:3] = 1,2,4

T = int(input())

for RPT in range(0,T):
    n = int(input())
    for rpt in range(3,n): 
        DP[rpt] = DP[rpt - 1] + DP[rpt - 2] + DP[rpt - 3]
    print(DP[n - 1],end="\n")