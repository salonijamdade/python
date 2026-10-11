a=input("enter one string")
cleaned=a.strip()
if cleaned==cleaned[::-1]:
    print("is palindrom")
else:
    print("not palindrome")