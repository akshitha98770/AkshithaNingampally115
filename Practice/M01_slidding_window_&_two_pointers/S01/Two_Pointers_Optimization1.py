a=list(map(int,input().split()))
i=0
for j in range(len(a)):
    if a[j]%2==0:
        a[i]=a[j]
        i+=1
print(a[:i])