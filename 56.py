ax=input().split()
a=ax[0]
b=ax[1]
for i in a:
    if i==b:
        print(a.index(i)+1)
        break
