n=[1,0,0,1,1]
i=0
sum=0
while i<len(n):
    a=n[-i-1]
    sum=sum+a*(2**i)
    i+=1
print(sum)