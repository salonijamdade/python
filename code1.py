text=" Welcome to imcc "

#remove space from first and last
print("remove space:",text.strip())

#convert the string to lower case
print("lower case:",text.lower())

#conver the string to upper case
print("upper case:",text.upper())

#capitalize first letter
a="hello world"
a=a.strip()
print("capitalized first letter:",a.capitalize())

#capitalize each word
print("capitalize each word:",text.title())

#count occurance of a substring
print("letter c occurs",text.count("c"))

#position of substring
print("position of  imcc substring",text.find("imcc"))

#replace
#it has two parameters one that we want to replace and second that 3hould be replaced
print("replace imcc with magic",text.replace("imcc","magic"))

#chech if string starts with or end with
print(text.startswith(" We"))
print(text.endswith("c "))

#split function that will spilt the string into a list
print("simple split",text.split())

text="ha"
a=" Welcome to imcc "
print(text+a)

list=[]
print(list)

fruits=["apple","banana","mango"]

number=[1,2,3,4,5]
print(number[-2])

number.append(6)
print(number)

fruits.insert(1,"cherry")
print(fruits)

number.remove(3)
print(number)

number.pop()
print(number)

#length of list
print("length of list number:",len(number))


#ascending order
print("ascending order of number list:",sorted(number))

#descending order
print("descending order of number list:",sorted(number,reverse=True))


