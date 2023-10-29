class Employee:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")

    # @classmethod #classmethod decorator is used to directly change the variable of class if it is used then the company name is changed to tesla.
    def changeCompany(cls, newCompany): #can write anything in place of cls like nischal, self, etc
        cls.company = newCompany

e1=Employee()
e1.name="Nischal"
e1.show()
e1.changeCompany("Tesla")  #It is like function
e1.show()
print(Employee.company) #doesnt change company to tesla it will be apple itself