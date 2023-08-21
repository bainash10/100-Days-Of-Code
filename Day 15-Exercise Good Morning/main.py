#Note the time module is built in module in python
import time
t=time.strftime('%H:%M:%S') #time.strftime() is a function used to return local time
print(t)
if(int(time.strftime('%H'))<12):
    print("Good Morning")
elif(int(time.strftime('%H'))>=12 or int(time.strftime('%H'))<17):
    print("Good Afternoon")
elif(int(time.strftime('%H'))>=17 or int(time.strftime('%H'))<19):
    print("Good Evening")
else:
    print("Good Night")

#Logical Operators in python are and, or, not