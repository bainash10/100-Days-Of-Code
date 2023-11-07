#single Inheritance is most common type of Inheritance
#from one parent class to child class
#very simple
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

d=Dog("Dog","Germansephard")
d.make_sound()

a=Animal("Dog","Pitbull")
a.make_sound()


#Quick Quiz:
# Implementing a cat class by using the animal  class. Adding some methods specific to cat 
print("----------Quick Quiz Solution---------------")
class cat(Animal):
    def __init__(self, name, species):
        Animal.__init__(self, name, species="Cat")
        self.species = species

    def make_sound(self):
        print("Meowww!")

c=cat("Cat","leopard")
c.make_sound()

e=Animal("Cat","Tiger")
e.make_sound()