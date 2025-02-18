def product(l):
    plst=[]
    for i in range(0,len(l)):
        prod=1
        for j in range(0,len(l)):
            if(l[i]!=l[j]):
                prod=prod* l[j]
        plst.append(prod)
    return plst
l=list(map(int,input().split()))
print(product(l))
