'''class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

e1=Employee("Nischal",12000)
print(e1.name)
print(e1.salary)

string="Nischal-12000"
e2=Employee(string.split("-")[0],string.split("-")[1])
#split method is used to split the word into the list that is Nischal and 12000 is kept into list
print(e2.name)
print(e2.salary)'''

#Using class methods
class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    @classmethod  #it is a alternative constructors 
    def fromStr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
    #typecasting because 12000 is an integer
    #if parsed using string.split it returns string itself
    
e1=Employee("Nischal",12000)
print(e1.name)
print(e1.salary)

string="Nischal-12000"
e2=Employee.fromStr(string)
print(e2.name)
print(e2.salary)

#example 2
print("----EG2----")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
    
person = Person.from_string("John Doe, 30")
print(person.name,person.age)
