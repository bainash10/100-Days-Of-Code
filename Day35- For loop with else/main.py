for i in range(5):
    print(i)
else:
    print("Sorry no i")

print("with empty list")
for i in []: #with empty list then else condition is executed
    print(i)
else:
    print("Sorry no i")


for i in range(6):
    print(i)
    if i == 4:
        break
else:  #not executed because loop is broken and out of the loop here break acts as the loop is successfully executed till last so else condition is not executed 
    print("Sorry no i")

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")