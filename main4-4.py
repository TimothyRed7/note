n=[]
n.append(int(input('num 1')))
n.append(int(input('num 2')))
y=0
x=1
for z in range(len(n),6):
    t=n[y]+n[x]
    n.append(t)
    y= y+1
    x=x+1
print(n)


