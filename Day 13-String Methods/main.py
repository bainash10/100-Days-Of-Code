#strings are immutable-->that means cannot be changed for existing string
a= "Nischal"
b= "Nischal!!! !!!! !!!"

print(len(a))

print(a.upper()) #Return a copy of the string converted to uppercase.

print(a.lower()) #Return a copy of the string converted to lowercase.

print(a.rstrip("!")) #Return a copy of the string with trailing whitespace removed. strip means 
#Remember that the strip(), lstrip(), and rstrip() methods create and return a new string with the desired modifications while leaving the original string unchanged.
#strip() method is a built-in string method that is used to remove leading and trailing whitespace characters (spaces, tabs, newlines) from a string. simply strip-->Remove 

print(a.replace("Nischal","Baidar"))

print(b.split(" "))

blogHeading = "introduction tO JS"

print(blogHeading.capitalize()) #returns first character of sentence to capital and other to lowercase. 

str1 = "Welcome to the Console!!!"
print(len(str1))

print(len(str1.center(50))) #Return a centered string of length width.

print(a.count("Nischal"))

print(str1.endswith("!!"))

print(str1.endswith("to", 4, 10)) # 4:10 slicing

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is")) #if not found returns -1
print(str1.index("is")) #if not found returns error

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) #if characters and numeric then returns true 

str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas"
print(str1.isprintable()) #if \n is present not printable

str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())