# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# sum=0
# for i in marks:
#     if isinstance(i,list):
#         for a in i:
#             sum=sum+a
#     else:
#         sum+=i
# print(sum)

marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
i=0
a=[]
while i<len(marks):
    j=0
    while j<len(marks[i]):
        a.append(marks[i][j])
        j+=1
    i+=1
print(a)

