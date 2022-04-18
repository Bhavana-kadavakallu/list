marks=[23,45,67,89,90,54,34,21,34,23,19,28,10,45,86,87,9]
length=len(marks)
index=0
less_than_50=0
more_than_50=0
while index<length:
    marks=marks[index]
    if marks<50:
        less_than_50+=1
    else:
        more_than_50+=1
    index+=1
print("marks more than 50:",str(more_than_50))
print("marks less than 50:",less_than_50)