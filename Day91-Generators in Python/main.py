#generators are different from list as list stores values
#it doesnot store values but stores information to generate values at that instant

#Remember if a function is using yield keyword then understand it is a generator.
def my_generator(): #generator doesnot occupies memory space as list does for its values 
    for i in range(5):
        yield i  #if used generator use yield instead of return

gen = my_generator()
# method 1 of printing
print(next(gen))
print(next(gen))
print(next(gen))
print("----------------------")
#method 2 to use generator for output showing
for j in gen:
    print(j)

#Benefits of Generators:
#allows to generate values on the fly 
#powerful tool for working with large or complex data sets
#doesnot occupy memory as list, tuples and sets
#They are lazy as it generates values only if needed 
