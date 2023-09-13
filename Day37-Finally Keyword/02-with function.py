def fun1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always executed")
    
def fun2():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    
print("I am not executed")

x=fun1()
print(x)
y=fun2()
print(y)