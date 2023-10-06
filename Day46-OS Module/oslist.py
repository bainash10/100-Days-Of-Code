import os
folders= os.listdir("data")
print(folders,"\n")

# os.chdir() --> Changes path of directory

print(os.getcwd())  #gets current working directory

print("\n")

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}")) #list of files or folders inside folder