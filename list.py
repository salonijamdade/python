list1=[1,2,3,"saloni",33,"sae","smita"]
number=[]
name=[]
for i in list1:
    if type(i)==int:
        number.append(i)
    else :
        name.append(i)

print(number)
print(name)

sorted_num=sorted(number)

print("highest number",number[-1])

