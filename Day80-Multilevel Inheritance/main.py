#from one child class to another child class 
#this type of inheritance is used to give hieararchy systems
#for eg like grandfather and grandson
#like A to B and from B to C
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o = GoldenRetriever("Tommy", "Black")
o.show_details() #first animal prints then dog and then lastly goldenretriever

print("------------")
d =Dog("Tommy", "blue")
d.show_details()

print("------------")
e =Animal("Tommy", "blue")
e.show_details()

#this inheritance gives advantage to reuse the code 