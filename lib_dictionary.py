lib={
    101:{"Name":"let us c","quantity":2},
    102:{"Name":"python","quantity":1},
    103:{"Name":"data structure and algorithm","quantity":5},
    104:{"Name":"DSA using c++","quantity":6},
    105:{"Name":"java","quantity":3}

}
check=input("check if the book is available from this list[let us c,python,data structure and algorithm,DSA using c++,java]:")
for sid,details in lib.items():
    if check==details["Name"]:
        print("book is available")
    else:
        print("not available")
