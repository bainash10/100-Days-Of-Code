# In Python, a lambda function is a small anonymous function without a name.

# def double(x):
#     return x*2 #is same as following with lambda functions
#used it for small functions in python
#use it for one line functions
double = lambda x:x*2
cube = lambda x: x**3  #x**3 is x*x*x
avg = lambda x, y, z: (x+y+z) / 3
def apple(fx, value):
    return 6 + fx(value)

print(double(5))
print(cube(5))
print(avg(3,5,10))
print(apple(lambda x:x*x, 2))  #these are anonymous functions as no name for functions passed functions in functions