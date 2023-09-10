# docstrings are the string literals that appear right after the definition of a function, method, class, or module.
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
    
square(5)
print(square.__doc__) #Printing Docstrings
#if changed docstring output of program can be changed whereas changing comment doesnt change the output