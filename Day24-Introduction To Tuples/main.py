tup =(1,2,3) #Typles cannot be changed, enclosed in normal bracket
print(tup)
print(type(tup))
print(len(tup))

tup =(1,2,3, "Green", True) 
print(tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[-1])

if 2 in tup:
    print("\n \tYes present")

#Slicing can be done in tuple
tup2 = tup[1:4]
print(tup2)