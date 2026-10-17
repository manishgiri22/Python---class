#function overloading 
class A:
    def __init__(self,i):
        self.i=i
    def __add__(self,other):
        return "{self.obj1} + {self.obj2}"
obj1=A(500)
obj2=A(250)
print(obj1+obj2)
