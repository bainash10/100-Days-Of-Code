import os

files = os.listdir("Day75-Exercise 7 Solution Clear The Clutter/clutteredFolder") #shows the files
i = 1
for file in files:
  if file.endswith(".png"): #checks if the file ends with the extension .png
    print(file)
    os.rename(f"Day75-Exercise 7 Solution Clear The Clutter/clutteredFolder/{file}", f"Day75-Exercise 7 Solution Clear The Clutter/clutteredFolder/{i}.png")
    i = i + 1
print("Therefore the files are renamed")