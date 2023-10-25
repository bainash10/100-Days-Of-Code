class Math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        self.num = self.num+n

    @staticmethod   #like normal method but inside class but doesnot require self
    def add(a, b):
        return a + b

result = Math.add(1, 2)
print(result) # Output: 3

a= Math(5)
print(a.num) #op 5

a.addtonum(6)
print(a.num) #op 11

print(a.add(7,2)) #op is 9 
#static methods can be called using classname dot or object dot

print(Math.add(7,2)) #op is 9 

# Interview Question: For a method to be created on class it is not necessary to keep self as an argument in method as static method doesnt take self as an argument