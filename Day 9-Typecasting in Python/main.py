#conversion of the datatype

a= "1"
b= "2"
print(a+b,"\n")
# o/p 12 as string 

a= "1"
b= "2"
print(int(a)+int(b))  #typecasting of string into int type 

# There are two types of typecasting 
# 1. Explicit --> Done by developer manually as per requirement
# 2. Implicit --> Done by interpreter itself automatically

#Implicit
c=1.8 #float
d=8  #int
print(c+d) #Ans 9.8, Automatically converts from lower to higher datatype

string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)