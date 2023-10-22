# When made a class in OOP the variables of the class are public by default.
'''class Employee:
    pass #pass means nothing

a = Employee()
a.emp1=5'''

#Access Specifiers /Modifiers are used to assign variables boundary

#PUBLIC:
#public means can be accessed by anywhere in program
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"Harry")
print(obj.age)  #can be accessed
print(obj.name)

print("----------------")

#PRIVATE:
# We cannot use private members outside of class.
# Can be made private by using __ double underscore before variable name. eg= self.__name
#Cannot be accessed directly outside the class for private variables but can be accessed using double underscores

class Student:
    # constructor is defined
    def __init__(self):
        self.__name = "Nischal"           # private variable

obj = Student()
# print(obj.__name) #cannot be accessed directly 
print(obj._Student__name) #can be accessed indirectly which means 'name mangling in python'.
# Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses.
# print(obj.__dir__()) #shows what are the methods and attributes that can be used 

print("-------------")

#Mangling and Non Mangling in Python
class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute


print("-------------")

#PROTECTED:
# In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e. a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses.

#The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName()) 