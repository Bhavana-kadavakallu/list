# magic=[[8,3,4],[1,5,9],[6,7,2]]
# print(magic[0][0])
# print(magic[0][1])
# print(magic[0][2])
# print(magic[1][0])
# print(magic[1][1])
# print(magic[1][2])
# print(magic[2][0])
# print(magic[2][1])
#   print(magic[2][2])

magic_square = [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
i=0
a=[]
b=[]
c=[]
while i<len(magic_square):
    a.append(magic_square[0][i])
    b.append(magic_square[1][i])
    c.append(magic_square[2][i])
    i+=1
print(a)
print(b)
print(c)

# magic_square = [[8, 3, 4],[1, 5, 9],[6, 7, 2]]
# i=0
# a=[]
# while i<len(magic_square):
#     j=0
#     while j<len(magic_square[i]):
#         a.append(magic_square[i][j])
#         j+=1
#     i+=1
# print(a)