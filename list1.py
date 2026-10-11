n=int(input("enter length of list"))

list=[]
for i in range(n):
    a=float(input("enter elements"))
    list.append(a)

print(list)
sum=0
for i in list:
    sum=sum+i
print(sum)


b=int(input("insert element at the third position"))

list.insert(2,b)

print(list)



