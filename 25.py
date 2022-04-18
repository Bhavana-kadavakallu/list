e=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum=0
sum1=0
while i<len(e):
    if e[i]%2==0:
        sum+=e[i]
    else:
        sum1+=e[i]
    i+=1
print("even=",sum)
print("odd=",sum1)