n=[50,40,23,70,56,12,5,10,7]
i=0
length=len(n)
max=0
while i<length:
    if n[i]>max:
        max=n[i]
    i+=1
print(max)