class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Nischal")
        super().parent_method() #calls parent method i.e super keyword is used to call methods of parentclass 

    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()

print("-----------Eg2--------------")

class ParentClass1:
    def parent_method(self):
        print("This is the parent method of ParentClass1.")

class ParentClass2:
    def parent_method(self):
        print("This is the parent method of ParentClass2.")

class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()

print("-----------Eg3--------------")

class Employee:
    def __init__(self,name, id):
        self.name=name
        self.id = id
        
class Programmer(Employee):
    def __init__(self,name, id,lang):
        self.lang =lang
        # self.name=name
        # self.id = id  #now to use the name and id of Employee we can use super keyword as the name and id of the employee is always same 
        super().__init__(name,id)

rohan=Employee("Rohan","420")
Nischal=Programmer("Nischal","421","Python")
print(rohan.name)
print(Nischal.name)
print(Nischal.lang)
print(Nischal.id)
        