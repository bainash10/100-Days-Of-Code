# Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types.

class vector():
    def __init__(self, i, j, k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i +{self.j}j+{self.k}k"
    def __add__(self,x):
        return vector(self.i +x.i, self.j+x.j, self.k+x.k)

v1=vector(3,5,6)
print(v1)
v2=vector(1,2,9)
print(v2)
print("The sum is:")
print(v1+v2)
print(type(v1+v2))