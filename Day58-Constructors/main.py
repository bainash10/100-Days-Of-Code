#Without using constructor
class Person:
    name = "Nischal"
    occ = "Developer"

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person()
print(a.name)
a.info()

print("________________")
#Constructor means special method to create and intialize an object of class
class Person:
    def __init__(self, n ,o): #whenever object is created this constructor is calloed
        print("hey I am a person")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Nischal", "Developer") #object created so hey i am a person is printed
b= Person("Bainash","Learner")  #object created so hey i am a person is printed
#self is automatically passed
a.info()
b.info()
#the main purpose is to initialize value when object is created

#When the constructor accepts arguments along with self, it is known as parameterized constructor.

# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.
