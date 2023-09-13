try:
    l = [1,5,6,7]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some error occured")
finally: #This block is executed always
    #difference of writing finally and only print function is if written in function and return a value from try and except block then if finally block is there then the code inside finally block is executed if the value is returned in beginning to
    print("I am always executed")
