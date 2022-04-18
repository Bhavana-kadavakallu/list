# magic_square =[[8, 3, 4],[1, 5, 9],[6, 7, 2]]
# i=0
# sum=0
# sum1=0
# sum2=0
# while i<len(magic_square):
#     j=0
#     while j<len(magic_square[i]):
#         if i==0:
#             sum=sum+magic_square[i][j]
#         elif i==1:
#             sum1=sum1+magic_square[i][j]
#         else:
#             sum2=sum2+magic_square[i][j]
#         j+=1
#     i+=1
# print(sum)
# print(sum1)
# print(sum2)
# if sum==sum1==sum2:
#     print("square")
# else:
#     print("not")


m=[[8,3,4],[1,5,9],[6,7,2]]
i=0
sum=0
sum1=0
sum2=0
while i<len(m):
    j=0
    while j<len(m[i]):
        if i==0:
            sum+=m[i][j]
        elif i==1:
            sum1+=m[i][j]
        else:
            sum2+=m[i][j]
        row=sum,sum1,sum2
        j+=1
    i+=1
print("row",sum)
print("row1",sum1)
print("row2",sum2)
print(row)
i=0
sum=0
sum1=0
sum2=0
while i<len(m):
    j=0
    while j<len(m[i]):
        if j==0:
            sum+=m[j][i]
        elif j==1:
            sum1+=m[j][i]
        else:
            sum2+=m[j][i]
        col=sum,sum1,sum2
        j+=1
    i+=1
print("col",sum)
print("col1",sum1)
print("col2",sum2)
print(col)
diagonal_right=0
diagonal_left=0
i=0
while i<len(m):
    j=0
    while j<len(m[i]):
        if i==j:
            diagonal_right+=m[i][j]
        if i+j==len(m[i])-1:
            diagonal_left+=m[i][j]
        diagonal=diagonal_right,diagonal_left
        j+=1
    i+=1
print(diagonal_right)
print(diagonal_left)
if col==row and diagonal_right==diagonal_left and sum==sum1==sum2:
    print("it s magic square")
else:
    print("it is not magic square")
