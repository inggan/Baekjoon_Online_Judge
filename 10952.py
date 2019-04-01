while True:
    case = list(map(int, input().split()))
    if sum(case) == 0:
        break
    print(sum(case))