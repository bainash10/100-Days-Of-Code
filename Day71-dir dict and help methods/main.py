#dir gives the method that can be used realted to that function
x = [1, 2, 3]
print(dir(x))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print("---------------------------------------------------------")
print(x.__add__)
print("---------------------------------------------------------")
y=(1,2)
print(dir(y))

print("---------------------------------------------------------")
# __dict__ is an attribute not a method.
# returns a dictionary representation of an object's attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1
p = Person("John", 30)
print(p.__dict__)

#help function is used to get documentation of attributes
print(help(Person))
print(help(__dict__))
