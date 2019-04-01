yut = {0:'E',1:'A',2:'B',3:'C',4:'D'}

for RPT in range(0,3):
    inp = input().split().count('0')
    print(yut.get(inp))