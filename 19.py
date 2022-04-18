num=30
n=[10,11,12,13,14,17,18,19]
i=0
while i<len(n)/2:
    j=0
    while j<len(n):
        if n[i]+n[j]==num:
            print([n[i],n[j]],end=" ")
        j+=1
    i+=1