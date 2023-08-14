a = 1 #a is a container (variable) where data is stored
print(a) #prints data of variable

b="Nischal" 
print(b)

c=True
print(c)

d=None
print(d)

e=complex(2,3) #for complex number
print(e)  #prints 2+3i, cannot assign as e=2+3i

print("Type of a is", type(a)) 
#type function returns the type of datatype used by variable.
print("Type of b is", type(b))
print("Type of c is", type(c))
print("Type of d is", type(d))
print("Type of e is", type(e))

#list is ordered collection of items of different datatypes
#list are mutable i.e can be changed
#list are inside square bracket
#sequence datatypes
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]  
print(list1)
print("Type of variable is", type(list1))

#tuple is ordered collection of items of different datatypes
#tuple are immutable i.e cannot be changed
#tuple are inside normal bracket()
#sequence datatypes
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
print("Type of variable is", type(tuple1))

#dictionary is unordered collection of items containing key:value pairs, i.e value of keys
#enclosed with curly braces
#mapped datatypes
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
print("Type of variable is", type(dict1))

#Note:
#In python everything is object so when printing type of, the o/p was <class 'datatype'>