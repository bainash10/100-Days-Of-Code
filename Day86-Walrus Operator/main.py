#new addition from python 3.8 onwards
#allows us to assign a variable within an expression

# a=True
# print(a=False) -> This forms an error
#Basic Expample:
a=True
print(a:=False)  #:= is a walrus operator

#use in while loop:
print("------------------------")
numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(numbers.pop())  #op is 5 4 3 2 1

#Example3:
print("------------------------")
happy = True
print(happy)

print("------------------------")
print(happy := True)

print("------------------------")

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)