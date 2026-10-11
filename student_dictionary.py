    #to access dictionary we use .item in for loop

#s
students={
    101:{"Name":"saloni","scores":[88,90,79]},
    102:{"Name":"sae","scores":[58,70,89]},
    103:{"Name":"smita","scores":[87,20]},
    104:{"Name":"jitendra","scores":[58,40,89]},
    105:{"Name":"bruno","scores":[25]}
}


#for calculation of avg and giving lables as avg and passed
for sid,details in students.items():
    avg=sum(details["scores"])/len(details["scores"])#use len function to get the avg
    details["avgrage"]=avg
    details["passed"]=avg>=30#boolen flag

#for printing passed students
print("students who passed")
for side,details in students.items():
    if details["passed"]:
        print(details["Name"])