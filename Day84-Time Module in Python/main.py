#Importance: timekeeping, formatting and conversions.
import time
def usingWhile():
    i=0
    while i<10:
        i=i+1
        print(i)
    

def usingFor():
    for i in range(10):
        print(i)
    
init=time.time()
usingFor()
t1=time.time()-init
init=time.time()
usingWhile()
print(t1)
print(time.time()-init)

time.sleep(3) #this will sleep the output printing for 3 sec
print("This is printed after 3 seconds")


t = time.localtime()  
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)  #this is to format the time 

print(formatted_time)
# Output: 2022-11-08 08:45:33
