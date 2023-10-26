class Employee:
    companyName = "Apple"
    noofemp=0
    #class variable is same for every instances 
    #Remember instances means objects
    def __init__(self,name):
        #instance variables are the variables that are associated with instances
        #instance variables can be changed
        self.name = name
        self.raise_amount = 0.02
        Employee.noofemp+=1
    
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noofemp} sized {self.companyName} is {self.raise_amount}")

emp1=Employee("Harry")
emp1.raise_amount=0.3
emp1.companyName = "Apple India"  #For harry changes company name to Apple India
emp1.showDetails()
# Employee.showDetails(emp1) #similar to above statement

print(Employee.companyName)
Employee.companyName="Google"
print(Employee.companyName)

emp2=Employee("Hari")
emp2.showDetails()

emp3=Employee("Nischal")
emp3.companyName="Self Comapny"
emp3.raise_amount=8
emp3.showDetails()