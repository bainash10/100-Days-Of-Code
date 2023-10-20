#Decorators modifies functions

def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

@greet  #method 1 to run
def hello():
    print("Hello")

#method 2 to run 
#greet(hello)()

hello()

print("-----Another Example------")

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

def add(a,b):
    print(a+b)

greet(add)(1,2)