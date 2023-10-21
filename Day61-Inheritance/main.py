#adding features inside existing class
class Employee:
    def __init__(self,name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee): #Inheritance
    def showLanguage(self): #Have characters of class Employee but it also have its own characteristics
        print("The default language is Python")

e1=Employee("Nischal" , 400)
e1.showDetails()
e2=Employee("Baidar" , 4200)
e2.showDetails()
e3=Programmer("Nischal",300)
e3.showLanguage()