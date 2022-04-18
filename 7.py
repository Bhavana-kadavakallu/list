n=[50,40,23,70,56,12,5,10,7]
i=0
length=len(n)
max=0
second_max=0
third_max=0
while i<length:
    if n[i]>max:
        max=n[i]
    elif n[i]>second_max and n[i]!=max:
        second_max=n[i]
    # elif n[i]>third_max and n[i]!=max and n[i]!=second_max:
    #     third_max=n[i]
    i+=1
print("1=",max)
print("2=",second_max)
# print("3=",third_max)