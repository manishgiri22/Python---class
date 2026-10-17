class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"square is {self.n*self.n}")
    def cuve(self):
        print(f"cuve is {self.n*self.n*self.n}")
sq= calculator(5)
sq.square()