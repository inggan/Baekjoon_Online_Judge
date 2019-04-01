K = int(input())
stack = list()

for i in range(0,K):
    N = int(input())
    if N == 0:
        stack.pop()
    else:
        stack.append(N)
print(sum(stack))