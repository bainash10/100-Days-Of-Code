#used in downloading a file from internet parallely
import threading
import time

#indicates some task being done
#the below example is doing the program one by one i.e only going to another function if one function is completed
# def func(seconds):
#     print(f"Sleeping for {seconds} seconds")
#     time.sleep(seconds)


# func(4)
# func(2)
# func(1)  

#Below example shows the example for multithreading
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

time1=time.perf_counter()
#Normal code
# func(4)
# func(2)
# func(1)  

# print(time2-time1) #time calculator in computing the codes

#Code using Threads
t1= threading.Thread(target=func, args=[4])
t2= threading.Thread(target=func, args=[2])
t3= threading.Thread(target=func, args=[1])

t1.start()  #this is used to start a threading process for t1
t2.start()
t3.start()

#By using join you wont be able to move to another function if one is not completed i.e t2 wont be executed if t1 is not completed hence it waits for t1
t1.join()
t2.join()
t3.join()

#Calculating Time
time2=time.perf_counter()
print(time2-time1)