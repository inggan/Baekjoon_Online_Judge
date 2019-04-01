N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cnt = 0

for i in range(0,N):
    A[i] = A[i] - B[0]
    if A[i] > 0:
        if A[i] % B[1] == 0:
            cnt += A[i] // B[1]
        else:
            cnt += (A[i] // B[1]) + 1
    cnt += 1

print(cnt)