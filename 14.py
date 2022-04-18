# l1=[1,2,3,4,5]
# l2=[2,3,1,0,6,7]
# for i in range(len(l1)):
#     for i in range(len(l2)):
#         if l1 not in l2:
#             print(i)

l1=[1,2,3,4,5,6]
l2=[2,3,1,0,6,7]
i=0
b=[]
while i<len(l1):
    if i not in l2:
        b.append(i)
    i+=1
print(b)