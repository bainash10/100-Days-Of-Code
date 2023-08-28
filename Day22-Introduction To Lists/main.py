#most used datatype
"""A list is similar to an array in other programming languages."""
#in list can add other data but in tuple cannot
l = [3,5,6]
print(type(l))
print(l)
print(l[0])
print(l[1])
print(l[2])

#In list can add data of different types.
l = [3,5,6,"Nischal", True] 
print(l)
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
print(l[-3]) #Negative Index -> to convert into positive index length of list - negative index
# i.e l[len(l)-3]
print(l[len(l)-3]) #length here is 5 so 5-3 i.e 2

# to check if data is present in list or not use if else statements
if 3 in l:
    print("Yes")
else:
    print("No")

#Same thing apply for string as well
if "is" in "Nischal":
    print("Yes")

print(l)
print(l[1:-1]) #slicing
#syntax -> listname[start : end : jumpIndex]
print(l[1:4:2]) 

#List Comprehension -> Creating lists using iteration
lst = [i for i in range(4)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)

