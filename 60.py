ax=input().split()
a=ax[0]
b=ax[1]
c=0
for i in range(0,len(ax)):
    for j in range(0,len(ax)):
        if a[i]==b[j]:
            c=1
            break
if c==1:
    print('yes')
else:
    print('no')
