list=[1,2,3,4,5,6,7,8,9,10]

#sum of last four elements
print('sum of last four pposition:',list[-4]+list[-3]+list[-2]+list[-1])

#remove the items from the list located at second and fifth position
print("remove the element from the seconf and fifth position:",list.pop(1),list.pop(3))
print(list)

#print the difference between highest and smallest in the list
sorted_list=sorted(list)
print(list)
print("difference between the highest and smallest in th elist is:",list[-1]-list[0])

#append a new element into the list which is half of the item of third positon in the list 
new=list[2]/2
list.append(new)
print("a new element into the list which is half of the item of third position in the list",list)


#sum of frist 10 element in the list

sum=0
for i in range(20):
    if i%2==0:
        sum=sum+i

print(sum)

#accept two variables S and N print square of numbers 

S=int(input("give starting number"))
N=int(input("give the ending number"))


for i in range(S,N+1):
    print(i**2)

#reverse the accepted string

text=input("enter one string")
print("reverse the string:",text[::-1])



#accept the sentence from user and count vowels

t1=input("enter the string")
print("count of vowels a:",t1.count("a"),"count of vowels e:",t1.count("e"),"count of vowels i:",t1.count("i"),"count of vowels o:",t1.count("o"),"count of vowels u:",t1.count("u"))

