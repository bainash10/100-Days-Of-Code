#Local variables are variables inside function
#Global variables are variables outside function
#local and global runs independently

#Program 1:
x=4 #Global Variable
print(x)

def hello():
    x=5 #local variable --> only accessible from function
    print(f"The local x is {x}")
    print("Hello")

print(f"The global x is {x}")
hello()
x=5
print(f"The global x is {x} \n")

#Program 2:
print("o/p of program 2 is")
x = 10 # global variable
def my_function():
  global x  #using global variable x
  x = 5 # this will change the value of the global variable x
  y = 5 # local variable

my_function()
print(x) # prints 5
#print(y)  this will cause an error because y is a local variable and is not accessible outside of the function

# It's important to note that it's generally considered good practice to avoid modifying global variables from within functions, as it can lead to unexpected behavior and make your code harder to debug.