#Set is a collection of unordered set of dataitems
#it doesnot show repeated items
#separated by commas inside curly braces
#Sets are unchangeable if once inserted
#Doesnt maintain order as inserted i.e can show different output according to different order
# Doesnt allow duplicate values
s = {2,4,2,6}
print(s)

info = {"Carla", 19, False, 5.9}
print(type(info))
print(info)

s={} #Type of this empty variable is dictionary
print(type(s)) 


nis=set() #TO create an empty set then use set() function
print(type(nis))

for value in info:
    print(value)