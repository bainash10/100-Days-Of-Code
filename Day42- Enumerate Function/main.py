marks = [12, 56, 32, 98, 12, 45, 1, 4]

#Normal Method
"""index=0
for mark in marks:
    print(mark)
    if(index == 3): #linter which means showing obvious error by curved underline
        print("Harry, awesome!")
    index+=1"""


for index, mark in enumerate(marks): #By default index starts with 0 prints below 98
    print(mark)
    if(index == 3): 
        print("Harry, awesome!")

print("\n \n")

for index, mark in enumerate(marks, start=1): #Can change starting index like in this example prints above 98
    print(mark)
    if(index == 3): 
        print("Harry, awesome!")