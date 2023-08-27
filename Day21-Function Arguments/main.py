def average(a,b):
    print("The average is", (a+b)/2)
average(4,6)

#default argument
def average(a=9, b=6):
    print("The average is", (a+b)/2)
average(1,5)
average(9)
average(b=9)
average()

#keyword argument
average(b=9,a=21) #doesnt matter arguments order by key=value syntax

#required argument 
#-> must give value for that argument in following example a is required argument
def average(a, b=6):
    print("The average is", (a+b)/2)
average(a=5)
average(5)
average(5,6)

def name(fname, mname, lname="System"):
    print("Hello,", fname, mname, lname)

name("Peter", "Quill")

#Arbitary arguments
def average(*numbers): #Takes parameters as a tuples
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))
    
average(1, 2, 3)

#Arbitary arguments
def average(**name): 
#Takes parameters as a dictionary requires key and value, takes name as a dictionary
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

#return statement-> returns value back to the calling function
def average(*numbers): #Takes parameters as a tuples
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)
    
c = average(1,2)
print(c)

#Note: When used *numbers then numbers is a tuple
#When used **numbers then numbers is a dictionaries