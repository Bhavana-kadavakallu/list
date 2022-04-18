n=[1,0,0,2,1]
i=0
sum=0
while i<len(n):
    a=n[-i-1]
    sum+=a*(2**i)
    i+=1
print(sum)