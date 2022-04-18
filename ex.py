n=[[1,2,3][4,5]]
i=0
n=str(n)
a=[]
while i<len(n):
    j=0
    while j<len(n[i]):
        a.append(int(n[i][j]))
        j+=1
    i+=1
print(a)