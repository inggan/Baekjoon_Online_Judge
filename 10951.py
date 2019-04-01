while True:
    try:
        N = list(map(int,input().split()))
        print(sum(N))
    except EOFError:
        break