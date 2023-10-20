class MyClass:
    def __init__(self, value):
        self._value = value
    
    def show(self):
        print(f"Value is {self._value}")

    @property  
    def ten_value(self): #this function is getter, this is the method of encapsulation. 
        return 10* self._value
    
    @ten_value.setter #This is setter, syntax is name.syntax where name is anything you can type.
    def ten_value(self, new_value):
        self._value = new_value/10
    
#property and ten_value.setter are decorators.
obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()