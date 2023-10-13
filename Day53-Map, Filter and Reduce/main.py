def cube(x):
    return x*x*x
print(cube(2))

#Normal method to cube the items of list l
l=[1,2,3,4,5] 
newl=[]
for item in l:
    newl.append(cube(item))
print(newl)

#using map 
l=[1,2,3,4,5] 
newl = list(map(cube,l))  #cube is function as argument, map is higher order function which means take function as argument
print(newl)
print(type(newl))

#map using lambda function
l=[1,2,3,4,5] 
newl = list(map(lambda x: x*x*x,l)) 
print(newl)

#filter--> higher order function
def filter_function(a): #filter function returns true or false if returned true then it is shown on output
    return a>4
newnewl = list(filter(filter_function,l))
print(newnewl)


#reduce
from functools import reduce  #need to import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers) #initially x is 1 and y is 2

# Print the sum
print(sum)

