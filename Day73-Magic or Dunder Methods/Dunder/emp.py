#magic method is used to give powerful way to manupulate objects and their behaviour.
class Employee:
    def __init__(self,name) -> None:
        self.name=name
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i

    def __str__(self):
        return f"The name is {self.name} str"
    
    def __repr__(self):
        return f"The name is ('{self.name}') repr"
    
    def __call__(self):
        print("I am Nischal")