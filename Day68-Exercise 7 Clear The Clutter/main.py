import os
files = os.listdir("Day68-Exercise 7 Clear The Clutter/data")
print("The files in the data folder that are cluttered are: \n",files)
print("-----------------------------------------------------------")
i=1
for file in files:
    if file.endswith(".png"):
        os.rename(f"Day68-Exercise 7 Clear The Clutter/data/{file}",f"Day68-Exercise 7 Clear The Clutter/data/{i}.png")
        i=i+1
        
files = os.listdir("Day68-Exercise 7 Clear The Clutter/data")
print("The renamed files in the data folder are: \n",files)