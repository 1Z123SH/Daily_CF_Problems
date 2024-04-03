q=(5**(1/2)+1)/2
a=input()
b=input()
a1=len(a)
b1=len(b)
ans1=0
ans2=0
for i in range(a1):
    ans1+=int(a[i])*q**(a1-i-1)
for i in range(b1):
    ans2+=int(b[i])*q**(b1-i-1)
if ans1>ans2:
    print('>')
elif ans1==ans2:
    print('=')
else:
    print('<')
