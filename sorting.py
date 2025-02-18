def sorting(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if(lst[i] < lst[j]):
                lst[i],lst[j]= lst[j],lst[i]
    return lst
lst=list(map(int,input().split()))
print(sorting(lst))