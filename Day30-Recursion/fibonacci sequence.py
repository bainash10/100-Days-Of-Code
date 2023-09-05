#Fibonacci
# f0 = 0
# f1 = 1
# f2 = f(1) + f(0)
# f(n) = f(n-1) +f(n-2)

def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))
     
# take input from the user  
n = int(input("How many terms? ")) 

# check if the number of terms is valid  
if n <= 0:  
   print("Please enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(n):  
       print(recur_fibo(i))  
    