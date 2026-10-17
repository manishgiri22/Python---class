#write a program to dispaly 2dvector and 3d vector using super keyword
class Twodvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f" the two D vector is : {self.i}i + {self.j}")
class Threedvector(Twodvector):
    def __init__(self,i,j,k):
        super().__init__(i,j) #super keyword then declaration the above function 
        self.k=k
    def show(self):
        print(f"the three D vector is : {self.i}i + {self.j}i + {self.k}")
a=Twodvector(1,5)
a.show()
b=Threedvector(12,5,9)
b.show()