alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
ans = input()

for rpt in alpha:
    ans = ans.replace(rpt,'*')

print(len(ans))