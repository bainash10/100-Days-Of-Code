#Importing in py means loading of code from a Python Module into the current script

import math #Can use var and functions defined in the module math
result=math.floor(4.2343)
print(result)

import math
result = math.sqrt(9)
print(result)  # Output: 3.0

from math import sqrt, pi
result = sqrt(9)*pi
print(result) 

# from math import *    -->If used * can import all functions and variables using the * wildcard, but not a great approach to practice only import the required variables and functions only.

from math import pi, sqrt as s  #sqrt as s
result = s(9)*pi
print(result) 

import math as m  #math as m
result=m.sqrt(9)
print(result)

import math
print(dir(math))  #dir functions shows what are the functions and variables inside the math module
print("\n")
print(math.nan,type(math.nan))

# import pandas as t
# print(dir(t))

from nis import welcome, nisc
welcome() #function in nis.py
print(nisc) #nisc is variable in file nis.py

import nis as n
n.welcome()
n.nisc
