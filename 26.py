e=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum=0
sum1=0
c=0
c1=0
while i<len(e):
    if e[i]%2==0:
        sum+=e[i]
        c+=1
    else:
        sum1+=e[i]
        c1+=1
    i+=1
print("avg of even=",sum/c)
print("avg of odd=",sum1/c1)