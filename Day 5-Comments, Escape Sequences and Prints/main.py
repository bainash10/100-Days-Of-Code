"""print("Hey I am Nischal
     and you are?")""" #cannot write like this so we need escape sequence

print("Hey I am Nischal \nand you are?") 
"""Put escape sequence with backslash (\n)"""

# (CTRL + /) is shortcut for keeping comments

"""This is a multi line comment"""
'''This is also multi line comment'''
#This is single line comment

#print("I am "Nischal"") #this is error: double quote inside double quote 
print("I am \"Nischal\"") #Output: I am "Nischal".
# Here \" is treated as a single character by Python interpreter

print ("Hey", 6, 7, sep="~") 
#separates values with tilde sign 
# Output: Hey~6~7

print ("Hey", 6, 7, sep="NULL") 

#sep and end are parameters in python
print("Hey", 6, 7, sep="~", end="009\n")  #at end 009 prints

print("Hey", 6, 7, sep="~", end="NULL\n") 

# Default separator is space and default end is New Line

print('Hey')
print('Hey')