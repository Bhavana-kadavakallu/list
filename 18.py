marks =[[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
i=0
sum=0
sum1=0
sum2=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        if i==0:
            sum=sum+marks[i][j]
        elif i==1:
            sum1=sum1+marks[i][j]
        else:
            sum2=sum2+marks[i][j]
        j+=1
    i+=1
print("avg1=",sum/len(marks[0]))
print("avg2=",sum1/len(marks[1]))
print("avg3=",sum2/len(marks[2]))
