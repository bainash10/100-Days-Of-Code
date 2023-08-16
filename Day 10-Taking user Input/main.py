a=input() #to take user input
print(a)
print("My name is", a)
a=input("Enter your name:")
print("My name is", a)

#Note:
#input funtion always takes every input as a string so when we take input as 12 and 100 and assign it to x and y respectively then the answer will not be 120 when added rather it will be 12100 because input funtion is not intelligent enough to convert the inputted number itself
#for this problem we can use typecasting

x=input("Enter first number")
y=input("Enter second number")
print(x+y) #it concatinates the user inputted number so to print the summation we require typecasting
print(int(x)+int(y)) #this prints the actual summation
print(float(x)+float(y)) 
