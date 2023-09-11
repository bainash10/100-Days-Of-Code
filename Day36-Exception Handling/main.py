a= input("Enter the number:")
print(f"Multiplication table of {a} is:")
try:
   for i in range(1,11):
        print(f"{int(a)} X {i}={int(a)*i}")
except Exception as e:
   print("Sorry")

#print("End")
#use exception handling when there might be error in program and to divert the error and not make the program to get into halt

try:
    num = int(input("Enter an integer: "))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error")