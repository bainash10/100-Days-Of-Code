#function that probide user to interact with the OS. 
#For eg automate to create folders in computer
import os

if(not os.path.exists("data")): # Test whether a path exists. Returns False for broken symbolic links
    os.mkdir("data") #creates a folder named data

for i in range(0,3):
    os.mkdir(f"data/Day{i+1}") #creates folder inside data folder
 
