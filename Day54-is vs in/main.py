# == compares value and is compares identity i.e it means is it same
#both are comparing operators
a = 4
b = "4"
print(a is b) #exact location of object in memory
print(a == b) #value
print("------")

a = [1,2,43]
b = [1,2,43]
print(a is b) 
print(a == b) 
print("------")

a = 3
b = 3
print(a is b) 
print(a == b) 
print("------")

a = "Nisc"
b = "Nisc"
print(a is b) 
print(a == b) 
print("------")

a = (1,2)
b = (1,2)
print(a is b) 
print(a == b) 
print("------")

a = None
b = None
print(a is b) 
print(a == b) 
print("------")

a = None
b = None
print(a is b) 
print(a == None) 
print("------")

