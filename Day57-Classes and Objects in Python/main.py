class Person:  #class is a blueprint like a place holder
    name = "Nischal"
    occupation = "Student"
    networth = 1
    def info(self):  
    #self here is a refrence to the current instance of the class and is used to access variables that belongs to the class
    #self is a person for which a method is being called
        print(f"{self.name} is a {self.occupation}")


a = Person() #object are the instances of a class
b= Person()
c= Person()
print(a.name)
a.info()
print("---------------")

b.name = "Shubham"
b.occupation = "Accountant"
print(b.name,b.occupation)
b.info()
print("---------------")

c.info()