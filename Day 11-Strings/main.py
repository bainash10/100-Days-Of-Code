name="Nischal"
friend="Bai"
anotherFriend = 'Bain'
apple= 'He said, "I want to eat an apple".'
banana= "He said, \"I want to eat an apple\"." #using escape sequence
a= '''Nisc
baina
hello''' #multi line printing without using new line character can use three single quote or double quote


print("Hello, "+name)
print(apple)
print(banana)
print(a)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
# print(name[7]) #Throws an error
print("Loop\n")
for character in name:
    print(character)


for character in a:
     print(character)
#NOTE:
#gives first element-->Index always starts with 0
#Strings is like an array of characters not exactly like array of characters