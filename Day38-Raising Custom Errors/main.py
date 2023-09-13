a= int(input("Enter any value between 5 and 9"))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")
#By using raise keyword custom errors can be raised
#to check different built in error checks, write "builtin errors in python" in GOOGLE

#Quick Quiz Solution
a= input("Enter any string")
if(a == "quit"):
    print(a)
else:
    raise ValueError("Enter other words")