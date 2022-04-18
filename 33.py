# question_list =["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]
# options_list =[["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"]["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
# solution_list = [3, 4, 1]
# print(len(question_list))
# i=0
# while i<len(question_list):
#     if i==0:
#         print(question_list[i])

question_list = [
["How many continents are there?"],
["What is the capital of India?"],
["NG mei kaun se course padhaya jaata hai?"]
]

options_list = [
["Four", "Nine", "Seven", "Eight"],
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
option50_50=[["1)four","3)seven"],["2)bhopal","4)delhi"],["1)software engineering","3)Tourism"]]
solution_list = [3, 4, 1]
print("KBC")
print("lets start the game")
i=0
c=0
s=10000
while i<len(question_list):
    print(question_list[i])
    a=0
    while a<len(options_list[i]):
        k=options_list[i][a]
        print(a+1,k)
        a+=1
    if c==0:
        life_line=input("do u want to use life line n/y:")
        if life_line=="yes":
            c+=1
            print(option50_50[i])
            s+=10000
    answer=int(input("enter the option"))
    if solution_list[i]==answer:
        print("answer is correct")
        print(s)
        s+=10000
    else:
        print("wrong")
        break
    i+=1
