l=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
i=0
c=0
c1=0
c2=0
c3=0
c4=0
c5=0
while i<len(l):
    if "a" in l[i]:
        c+=1
    elif "n" in l[i]:
        c1+=1
    elif "t" in l[i]:
        c2+=1
    elif "x" in l[i]:
        c3+=1
    elif "u" in l[i]:
        c4+=1
    else:
        c5+=1
    i+=1
print("a-",c,"times")
print("n-",c1,"times")
print("t-",c2,"times")
print("x-",c3,"times")
print("u-",c4,"times")
print("g-",c5,"times")
print([["a",c],["n",c1],["t",c2],["x",c3],["u",c4],["g",c5]])