from itertools import combinations_with_replacement
for k in range(int(input())):
    l=int(input())
    y=[0,1,2]
    s=0
    x=combinations_with_replacement(y,l)
    if l==1 or l==2:
        print(0)
    else:
        for i in x:
            for j in range(1,len(i)-1):
                if (i[j]>i[j+1] and i[j]>i[j-1]) or (i[j]<i[j+1] and i[j]<i[j-1]):
                    s+=1 
        print(s)