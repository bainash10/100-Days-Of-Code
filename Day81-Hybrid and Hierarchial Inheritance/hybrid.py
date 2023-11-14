#Hybrid inheritance is a combination of multiple inheritance and single inheritance in object-oriented programming. 
class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1, Derived2):
    pass