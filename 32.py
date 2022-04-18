# mainstr = ["the", "quick", "brown", "fox", "jumped","over", "the","lazy", "dog", "the", "dog", "slept", "over", "the", "verandah."]
# substr=["over"]
# i=0
# b=[]
# while i<len(mainstr):
#     if mainstr[i] not in substr:
#         b.append(mainstr[i])
#     i+=1
# print(b)


# m="the quick brown fox jumped over the lazy dog the dog slept over the varandha."
# a=m.split()
# b=""
# i=0
# while i<len(a):
#     if a[i]=="over":
#         a.remove("over")
#     b+=a[i]+" "
#     i+=1
# # print(a)
# print(b)


m="the quick brown fox jumped over the lazy dog the dog slept over the varandha."
a=m.split()
substr="over"
replacementstr="on"
b=""
print(a)
i=0
while i<len(a):
    if a[i]==substr:
        a[i]=replacementstr
    b+=a[i]+" "
    i+=1
# print(a)
print(b)

