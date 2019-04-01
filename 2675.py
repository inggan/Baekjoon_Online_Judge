T = int(input())
result = ""

for i in range(0,T):
    inp = input().split()
    for j in range(0,len(inp[1])):
        result += str(inp[1])[j] * int(inp[0])
    print(result)
    result = ""