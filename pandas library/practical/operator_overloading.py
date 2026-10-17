class Complexnumber:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,other):
        return f"{self.real+other.real} + {self.imaginary+other.imaginary}i"

c1=Complexnumber(2,3)
c2=Complexnumber(1,3)
print(c1+c2)