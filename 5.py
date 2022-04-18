n=[50,40,23,70,56,12,5,10,7]
i=0
length=len(n)
count=0
while i<length:
    if 20<n[i]<40:
        count=count+1
    i+=1
print(count)